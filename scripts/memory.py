# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "chromadb>=1.0.0",
#     "httpx>=0.27.0",
#     "numpy>=1.24.0",
# ]
# ///
"""
svvarm memory — Persistent, per-agent design memory with semantic search.

Markdown files are the source of truth. Embeddings are a derived cache.
Everything is per-project — no overlap between projects.

Embedding backends (configured in .svvarm/config.json):
  - "ollama"  — Ollama API (easiest, pull a model and go)
  - "llama"   — llama.cpp server (best quality with LCO model)
  - "openai"  — OpenAI API (requires API key)

Per-project storage:
  .svvarm/
  ├── config.json       ← Embedding backend config
  ├── context.md        ← Design brief (created by init/setup)
  ├── decisions.md      ← Decision log
  ├── .chromadb/        ← Vector index (rebuildable from .md files)
  └── memory/           ← Agent memories (source of truth)
      └── <agent>.md

Usage:
    uv run memory.py setup                          # First-time setup
    uv run memory.py save <agent> "<content>"       # Save to agent memory
    uv run memory.py search "<query>"               # Semantic search
    uv run memory.py recall <agent> --query "<q>"   # Full agent recall
    uv run memory.py index                          # Re-index memory files
    uv run memory.py read <agent>                   # Read agent's full memory
    uv run memory.py context                        # Read project context
    uv run memory.py status                         # Check system status
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

# ─── Defaults ──────────────────────────────────────────────────

DEFAULT_OLLAMA_MODEL = "bge-m3"
DEFAULT_OLLAMA_URL = "http://localhost:11434"
DEFAULT_LLAMA_URL = "http://localhost:8384"
DEFAULT_LLAMA_MODEL_PATH = os.path.expanduser(
    "~/.svvarm/models/LCO-Embedding-Omni-3B-Q8_0.gguf"
)

VALID_AGENTS = [
    "typography-lead",
    "color-lead",
    "layout-lead",
    "slop-auditor",
    "polish-lead",
    "production-lead",
    "content-lead",
    "cdo",
]


# ─── Config ────────────────────────────────────────────────────


def get_svvarm_dir(project_dir: str = ".") -> Path:
    return Path(project_dir).resolve() / ".svvarm"


def get_memory_dir(project_dir: str = ".") -> Path:
    d = get_svvarm_dir(project_dir) / "memory"
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_db_dir(project_dir: str = ".") -> Path:
    d = get_svvarm_dir(project_dir) / ".chromadb"
    d.mkdir(parents=True, exist_ok=True)
    return d


def get_global_dir() -> Path:
    d = Path.home() / ".svvarm"
    d.mkdir(parents=True, exist_ok=True)
    return d


def load_config(project_dir: str = ".") -> dict:
    """Load embedding config. Project config overrides global config."""
    config = {
        "backend": "ollama",
        "ollama_model": DEFAULT_OLLAMA_MODEL,
        "ollama_url": DEFAULT_OLLAMA_URL,
        "llama_url": DEFAULT_LLAMA_URL,
        "llama_model_path": DEFAULT_LLAMA_MODEL_PATH,
        "openai_api_key": "",
        "openai_model": "text-embedding-3-small",
    }

    # Global config
    global_config = get_global_dir() / "config.json"
    if global_config.exists():
        with open(global_config) as f:
            config.update(json.load(f))

    # Project config overrides global
    project_config = get_svvarm_dir(project_dir) / "config.json"
    if project_config.exists():
        with open(project_config) as f:
            config.update(json.load(f))

    return config


def save_config(config: dict, project_dir: str | None = None):
    """Save config. If project_dir given, save to project. Otherwise global."""
    if project_dir:
        config_file = get_svvarm_dir(project_dir) / "config.json"
    else:
        config_file = get_global_dir() / "config.json"
    config_file.parent.mkdir(parents=True, exist_ok=True)
    with open(config_file, "w") as f:
        json.dump(config, f, indent=2)


# ─── Embedding Backends ───────────────────────────────────────


def embed_ollama(texts: list[str], config: dict) -> list[list[float]]:
    """Get embeddings via Ollama API."""
    import httpx

    url = config.get("ollama_url", DEFAULT_OLLAMA_URL)
    model = config.get("ollama_model", DEFAULT_OLLAMA_MODEL)

    embeddings = []
    for text in texts:
        try:
            r = httpx.post(
                f"{url}/api/embed",
                json={"model": model, "input": text},
                timeout=60.0,
            )
            r.raise_for_status()
            data = r.json()
            # Ollama returns {"embeddings": [[...], ...]}
            if "embeddings" in data and data["embeddings"]:
                embeddings.append(data["embeddings"][0])
            elif "embedding" in data:
                embeddings.append(data["embedding"])
            else:
                raise ValueError(f"Unexpected response format: {list(data.keys())}")
        except httpx.ConnectError:
            print(
                f"ERROR: Ollama not running at {url}\n"
                f"  Start Ollama and pull the model:\n"
                f"    ollama pull {model}",
                file=sys.stderr,
            )
            sys.exit(1)
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 404:
                print(
                    f"ERROR: Model '{model}' not found in Ollama.\n"
                    f"  Pull it with: ollama pull {model}",
                    file=sys.stderr,
                )
                sys.exit(1)
            raise

    return embeddings


def embed_llama(texts: list[str], config: dict) -> list[list[float]]:
    """Get embeddings via llama.cpp server."""
    import httpx

    url = config.get("llama_url", DEFAULT_LLAMA_URL)

    try:
        r = httpx.post(
            f"{url}/embeddings",
            json={"content": texts},
            timeout=60.0,
        )
        r.raise_for_status()
        data = r.json()

        if "results" in data:
            return [item["embedding"] for item in data["results"]]
        elif "data" in data:
            return [item["embedding"] for item in data["data"]]
        elif isinstance(data, list):
            return data
        else:
            raise ValueError(f"Unexpected response: {list(data.keys())}")

    except httpx.ConnectError:
        print(
            f"ERROR: llama.cpp server not running at {url}\n"
            f"  Start it with:\n"
            f"    llama-server -m {config.get('llama_model_path', DEFAULT_LLAMA_MODEL_PATH)} "
            f"--embedding --pooling last --port 8384 -ngl 99",
            file=sys.stderr,
        )
        sys.exit(1)


def embed_openai(texts: list[str], config: dict) -> list[list[float]]:
    """Get embeddings via OpenAI API."""
    import httpx

    api_key = config.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print(
            "ERROR: No OpenAI API key. Set OPENAI_API_KEY env var or add to config.",
            file=sys.stderr,
        )
        sys.exit(1)

    model = config.get("openai_model", "text-embedding-3-small")

    r = httpx.post(
        "https://api.openai.com/v1/embeddings",
        headers={"Authorization": f"Bearer {api_key}"},
        json={"input": texts, "model": model},
        timeout=60.0,
    )
    r.raise_for_status()
    data = r.json()
    return [item["embedding"] for item in data["data"]]


def get_embeddings(texts: list[str], project_dir: str = ".") -> list[list[float]]:
    """Route to the configured embedding backend."""
    config = load_config(project_dir)
    backend = config.get("backend", "ollama")

    if backend == "none":
        return []
    elif backend == "ollama":
        return embed_ollama(texts, config)
    elif backend == "llama":
        return embed_llama(texts, config)
    elif backend == "openai":
        return embed_openai(texts, config)
    else:
        print(f"ERROR: Unknown backend '{backend}'. Use: ollama, llama, openai, none", file=sys.stderr)
        sys.exit(1)


def backend_is_available(project_dir: str = ".") -> bool:
    """Check if the configured embedding backend is responding."""
    import httpx

    config = load_config(project_dir)
    backend = config.get("backend", "ollama")

    if backend == "none":
        return False

    try:
        if backend == "ollama":
            url = config.get("ollama_url", DEFAULT_OLLAMA_URL)
            r = httpx.get(f"{url}/api/tags", timeout=3.0)
            return r.status_code == 200
        elif backend == "llama":
            url = config.get("llama_url", DEFAULT_LLAMA_URL)
            r = httpx.get(f"{url}/health", timeout=3.0)
            return r.status_code == 200
        elif backend == "openai":
            return bool(
                config.get("openai_api_key") or os.environ.get("OPENAI_API_KEY")
            )
    except Exception:
        return False

    return False


# ─── Chunking ──────────────────────────────────────────────────


def chunk_markdown(text: str, source: str, max_chunk_size: int = 1200) -> list[dict]:
    """Split markdown by headings. Each chunk gets metadata."""
    chunks = []
    current_heading = ""
    current_lines = []
    heading_level = 0

    for line in text.split("\n"):
        heading_match = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading_match:
            if current_lines:
                content = "\n".join(current_lines).strip()
                if content:
                    chunks.append({
                        "content": content,
                        "heading": current_heading,
                        "heading_level": heading_level,
                        "source": source,
                    })
            current_heading = heading_match.group(2)
            heading_level = len(heading_match.group(1))
            current_lines = [line]
        else:
            current_lines.append(line)

    if current_lines:
        content = "\n".join(current_lines).strip()
        if content:
            chunks.append({
                "content": content,
                "heading": current_heading,
                "heading_level": heading_level,
                "source": source,
            })

    # Split oversized chunks at paragraph boundaries
    final_chunks = []
    for chunk in chunks:
        if len(chunk["content"]) > max_chunk_size:
            paragraphs = chunk["content"].split("\n\n")
            current = ""
            for para in paragraphs:
                if len(current) + len(para) > max_chunk_size and current:
                    final_chunks.append({**chunk, "content": current.strip()})
                    current = para
                else:
                    current = current + "\n\n" + para if current else para
            if current.strip():
                final_chunks.append({**chunk, "content": current.strip()})
        else:
            final_chunks.append(chunk)

    return final_chunks


def content_hash(content: str) -> str:
    return hashlib.sha256(content.encode()).hexdigest()[:16]


# ─── ChromaDB with Custom Embeddings ──────────────────────────


class SVVarmEmbeddingFunction:
    """Custom ChromaDB embedding function using BGE-M3 via configured backend.
    Implements the ChromaDB v1 EmbeddingFunction interface."""

    def __init__(self, project_dir: str = "."):
        self.project_dir = project_dir

    def __call__(self, input: list[str]) -> list:
        import numpy as np

        embeddings = get_embeddings(input, self.project_dir)
        return [np.array(e, dtype=np.float32) for e in embeddings]

    def embed_query(self, input: list[str]) -> list:
        return self.__call__(input)

    @staticmethod
    def name() -> str:
        return "svvarm-bge-m3"

    @staticmethod
    def default_space() -> str:
        return "cosine"


def get_collection(project_dir: str = "."):
    """Get or create the per-project memory collection."""
    import chromadb

    db_path = str(get_db_dir(project_dir))
    client = chromadb.PersistentClient(path=db_path)

    collection = client.get_or_create_collection(
        name="svvarm_memory",
        embedding_function=SVVarmEmbeddingFunction(project_dir),
        metadata={"hnsw:space": "cosine"},
    )
    return collection


def index_memories(project_dir: str = ".") -> dict:
    """Index all memory markdown files into ChromaDB.
    Skips silently if no embedding backend is available."""
    if not backend_is_available(project_dir):
        return {"files": 0, "chunks": 0, "skipped": True}

    memory_dir = get_memory_dir(project_dir)
    svvarm_dir = get_svvarm_dir(project_dir)

    files_to_index = list(memory_dir.glob("*.md"))

    for name in ["context.md", "decisions.md"]:
        f = svvarm_dir / name
        if f.exists() and f.stat().st_size > 0:
            files_to_index.append(f)

    if not files_to_index:
        return {"files": 0, "chunks": 0}

    collection = get_collection(project_dir)
    total_chunks = 0

    for md_file in files_to_index:
        text = md_file.read_text()
        if not text.strip():
            continue

        source = md_file.stem
        chunks = chunk_markdown(text, source)
        if not chunks:
            continue

        ids = []
        documents = []
        metadatas = []

        for chunk in chunks:
            chunk_id = f"{source}_{content_hash(chunk['content'])}"
            ids.append(chunk_id)
            documents.append(chunk["content"])
            metadatas.append({
                "source": chunk["source"],
                "heading": chunk["heading"],
                "heading_level": chunk["heading_level"],
                "agent": source,
            })

        collection.upsert(ids=ids, documents=documents, metadatas=metadatas)
        total_chunks += len(chunks)

    return {"files": len(files_to_index), "chunks": total_chunks}


def keyword_search(
    query: str,
    project_dir: str = ".",
    agent: str | None = None,
    top_k: int = 5,
) -> list[dict]:
    """Fallback keyword search when no embedding backend is available.
    Searches markdown files directly using simple word matching."""
    memory_dir = get_memory_dir(project_dir)
    svvarm_dir = get_svvarm_dir(project_dir)

    files_to_search = list(memory_dir.glob("*.md"))
    for name in ["context.md", "decisions.md"]:
        f = svvarm_dir / name
        if f.exists() and f.stat().st_size > 0:
            files_to_search.append(f)

    if agent:
        files_to_search = [f for f in files_to_search if f.stem == agent]

    query_words = set(query.lower().split())
    matches = []

    for md_file in files_to_search:
        text = md_file.read_text()
        if not text.strip():
            continue

        chunks = chunk_markdown(text, md_file.stem)
        for chunk in chunks:
            content_lower = chunk["content"].lower()
            word_hits = sum(1 for w in query_words if w in content_lower)
            if word_hits > 0:
                score = round(word_hits / max(len(query_words), 1), 4)
                matches.append({
                    "content": chunk["content"],
                    "agent": chunk["source"],
                    "heading": chunk["heading"],
                    "score": score,
                })

    matches.sort(key=lambda x: x["score"], reverse=True)
    return matches[:top_k]


def search_memories(
    query: str,
    project_dir: str = ".",
    agent: str | None = None,
    top_k: int = 5,
) -> list[dict]:
    """Search across agent memories. Uses semantic search if an embedding
    backend is available, falls back to keyword search otherwise."""
    if not backend_is_available(project_dir):
        return keyword_search(query, project_dir, agent, top_k)

    collection = get_collection(project_dir)

    if collection.count() == 0:
        index_memories(project_dir)
        if collection.count() == 0:
            return []

    where = {"agent": agent} if agent else None

    results = collection.query(
        query_texts=[query],
        n_results=min(top_k, collection.count()),
        where=where,
        include=["documents", "metadatas", "distances"],
    )

    matches = []
    if results["documents"] and results["documents"][0]:
        for i, doc in enumerate(results["documents"][0]):
            meta = results["metadatas"][0][i] if results["metadatas"] else {}
            distance = results["distances"][0][i] if results["distances"] else 0
            matches.append({
                "content": doc,
                "agent": meta.get("agent", "unknown"),
                "heading": meta.get("heading", ""),
                "score": round(1 - distance, 4),
            })

    return matches


# ─── Memory File Operations ───────────────────────────────────


def save_memory(agent: str, content: str, project_dir: str = ".") -> str:
    """Append content to an agent's memory file with timestamp."""
    if agent not in VALID_AGENTS:
        print(f"ERROR: Unknown agent '{agent}'. Valid: {', '.join(VALID_AGENTS)}", file=sys.stderr)
        sys.exit(1)
    memory_dir = get_memory_dir(project_dir)
    memory_file = memory_dir / f"{agent}.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    if not memory_file.exists():
        memory_file.write_text(f"# {agent} — Design Memory\n\n")

    with open(memory_file, "a") as f:
        f.write(f"\n## {timestamp}\n\n{content}\n")

    # Re-index if backend available (non-fatal if not)
    if backend_is_available(project_dir):
        try:
            index_memories(project_dir)
        except Exception:
            pass

    return str(memory_file)


def read_memory(agent: str, project_dir: str = ".") -> str:
    """Read an agent's full memory file."""
    memory_file = get_memory_dir(project_dir) / f"{agent}.md"
    if memory_file.exists():
        return memory_file.read_text()
    return ""


def read_context(project_dir: str = ".") -> str:
    """Read the project design context."""
    f = get_svvarm_dir(project_dir) / "context.md"
    return f.read_text() if f.exists() else ""


def read_decisions(project_dir: str = ".") -> str:
    """Read the project decision log."""
    f = get_svvarm_dir(project_dir) / "decisions.md"
    return f.read_text() if f.exists() else ""


def recall_agent(
    agent: str,
    query: str | None = None,
    project_dir: str = ".",
    top_k: int = 5,
) -> dict:
    """Full agent recall: own memory + context + cross-agent search."""
    result = {
        "own_memory": read_memory(agent, project_dir),
        "context": read_context(project_dir),
        "decisions": read_decisions(project_dir),
        "cross_agent": [],
    }

    if query and backend_is_available(project_dir):
        try:
            all_results = search_memories(query, project_dir=project_dir, top_k=top_k)
            result["cross_agent"] = [r for r in all_results if r["agent"] != agent]
        except Exception:
            pass  # Graceful — markdown files still available

    return result


# ─── Setup & Server Management ────────────────────────────────


def run_setup(project_dir: str = "."):
    """Interactive first-time setup. Configures embedding backend."""
    import httpx

    print("=" * 60)
    print("  svvarm memory — first-time setup")
    print("=" * 60)
    print()

    # Step 1: Check what's available
    ollama_available = False
    llama_available = False

    try:
        r = httpx.get(f"{DEFAULT_OLLAMA_URL}/api/tags", timeout=3.0)
        ollama_available = r.status_code == 200
    except Exception:
        pass

    try:
        r = httpx.get(f"{DEFAULT_LLAMA_URL}/health", timeout=3.0)
        llama_available = r.status_code == 200
    except Exception:
        pass

    openai_key = os.environ.get("OPENAI_API_KEY", "")

    print("Detected:")
    print(f"  Ollama:      {'✓ running' if ollama_available else '✗ not detected'}")
    print(f"  llama.cpp:   {'✓ running' if llama_available else '✗ not detected'}")
    print(f"  OpenAI key:  {'✓ set' if openai_key else '✗ not set'}")
    print()

    # Step 2: Pick backend
    if llama_available:
        backend = "llama"
        print("Using: llama.cpp server (LCO-Embedding-Omni-3B)")
    elif ollama_available:
        backend = "ollama"
        print("Using: Ollama")

        # Check if embedding model is pulled
        try:
            r = httpx.get(f"{DEFAULT_OLLAMA_URL}/api/tags", timeout=5.0)
            models = [m["name"] for m in r.json().get("models", [])]
            has_embed_model = any(DEFAULT_OLLAMA_MODEL in m for m in models)

            if not has_embed_model:
                print(f"\n  Pulling embedding model: {DEFAULT_OLLAMA_MODEL}...")
                result = subprocess.run(
                    ["ollama", "pull", DEFAULT_OLLAMA_MODEL],
                    capture_output=False,
                    timeout=300,
                )
                if result.returncode != 0:
                    print(f"  WARNING: Failed to pull {DEFAULT_OLLAMA_MODEL}", file=sys.stderr)
                else:
                    print(f"  ✓ {DEFAULT_OLLAMA_MODEL} ready")
            else:
                print(f"  ✓ {DEFAULT_OLLAMA_MODEL} already available")
        except Exception as e:
            print(f"  WARNING: Could not verify model: {e}", file=sys.stderr)

    elif openai_key:
        backend = "openai"
        print("Using: OpenAI API (text-embedding-3-small)")
    else:
        backend = "none"
        print("No embedding backend detected — using keyword search fallback.")
        print()
        print("svvarm works without embeddings, but semantic search is better.")
        print("To enable it later, pick one:")
        print("  1. Install Ollama:  brew install ollama && ollama serve && ollama pull bge-m3")
        print("  2. Set OpenAI key:  export OPENAI_API_KEY=sk-...")
        print("  3. Run llama.cpp:   See README.md for LCO model setup")
        print()
        print("Then re-run: uv run memory.py setup")

    # Step 3: Save config
    config = {"backend": backend}
    if backend == "ollama":
        config["ollama_model"] = DEFAULT_OLLAMA_MODEL
        config["ollama_url"] = DEFAULT_OLLAMA_URL
    elif backend == "llama":
        config["llama_url"] = DEFAULT_LLAMA_URL
        config["llama_model_path"] = DEFAULT_LLAMA_MODEL_PATH
    elif backend == "openai":
        config["openai_api_key"] = "env:OPENAI_API_KEY"
        config["openai_model"] = "text-embedding-3-small"

    # Save globally (applies to all projects unless overridden)
    save_config(config)
    print(f"\n✓ Global config saved to ~/.svvarm/config.json")

    # Step 4: Test it (skip for "none" backend)
    if backend != "none":
        print("\nTesting embedding...")
        try:
            result = get_embeddings(["test embedding"], project_dir)
            dim = len(result[0])
            print(f"✓ Working! Embedding dimension: {dim}")
        except Exception as e:
            print(f"✗ Test failed: {e}", file=sys.stderr)
            sys.exit(1)

    # Step 5: Initialize project if .svvarm exists
    svvarm_dir = get_svvarm_dir(project_dir)
    if svvarm_dir.exists():
        print(f"\n✓ Project memory at: {svvarm_dir}")
    else:
        print(f"\nProject memory will be created when you run /svvarm init or /svvarm setup")

    print()
    if backend == "none":
        print("Setup complete! svvarm will use keyword search for memory.")
        print("Add an embedding backend anytime for better semantic search.")
    else:
        print("Setup complete! You can now use svvarm memory.")
        print()
        print("Upgrade to LCO-Embedding-Omni-3B for best quality:")
        print("  See: https://huggingface.co/marksverdhei/LCO-Embedding-Omni-3B-GGUF")


def show_status(project_dir: str = "."):
    """Show full system status."""
    import httpx

    config = load_config(project_dir)
    backend = config.get("backend", "ollama")

    print("svvarm memory status")
    print("=" * 40)

    # Backend
    available = backend_is_available(project_dir)
    print(f"Backend:    {backend} {'✓' if available else '✗ NOT RUNNING'}")

    if backend == "ollama":
        print(f"  URL:      {config.get('ollama_url', DEFAULT_OLLAMA_URL)}")
        print(f"  Model:    {config.get('ollama_model', DEFAULT_OLLAMA_MODEL)}")
    elif backend == "llama":
        print(f"  URL:      {config.get('llama_url', DEFAULT_LLAMA_URL)}")
        print(f"  Model:    {config.get('llama_model_path', DEFAULT_LLAMA_MODEL_PATH)}")
    elif backend == "openai":
        has_key = bool(config.get("openai_api_key") or os.environ.get("OPENAI_API_KEY"))
        print(f"  Model:    {config.get('openai_model', 'text-embedding-3-small')}")
        print(f"  API Key:  {'✓ set' if has_key else '✗ missing'}")

    # Project
    svvarm_dir = get_svvarm_dir(project_dir)
    if svvarm_dir.exists():
        print(f"\nProject:    {svvarm_dir}")
        print(f"  context.md:   {'✓' if (svvarm_dir / 'context.md').exists() else '✗'}")
        print(f"  decisions.md: {'✓' if (svvarm_dir / 'decisions.md').exists() else '✗'}")

        memory_dir = svvarm_dir / "memory"
        if memory_dir.exists():
            agents = list(memory_dir.glob("*.md"))
            print(f"  Agents:       {len(agents)} with memories")
            for a in sorted(agents):
                lines = len(a.read_text().split("\n"))
                print(f"    {a.stem}: {lines} lines")

        db_dir = svvarm_dir / ".chromadb"
        if db_dir.exists():
            try:
                collection = get_collection(project_dir)
                print(f"  Vector index: {collection.count()} chunks indexed")
            except Exception:
                print(f"  Vector index: exists (count unavailable)")
        else:
            print(f"  Vector index: not built yet")
    else:
        print(f"\nProject:    not initialized (run /svvarm init or /svvarm setup)")

    # Global
    global_config = get_global_dir() / "config.json"
    print(f"\nGlobal config: {'✓' if global_config.exists() else '✗ run: uv run memory.py setup'}")


# ─── CLI ───────────────────────────────────────────────────────


def main():
    parser = argparse.ArgumentParser(
        description="svvarm memory — persistent agent design memory"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # setup
    setup_cmd = subparsers.add_parser("setup", help="First-time setup")
    setup_cmd.add_argument("--project-dir", default=".", help="Project root")

    # status
    status_cmd = subparsers.add_parser("status", help="Show system status")
    status_cmd.add_argument("--project-dir", default=".", help="Project root")

    # save
    save_cmd = subparsers.add_parser("save", help="Save to agent memory")
    save_cmd.add_argument("agent", help="Agent name (e.g., typography-lead)")
    save_cmd.add_argument("content", help="Content to save")
    save_cmd.add_argument("--project-dir", default=".", help="Project root")

    # search
    search_cmd = subparsers.add_parser("search", help="Semantic search")
    search_cmd.add_argument("query", help="Search query")
    search_cmd.add_argument("--agent", help="Filter to specific agent")
    search_cmd.add_argument("--top-k", type=int, default=5)
    search_cmd.add_argument("--project-dir", default=".", help="Project root")

    # recall
    recall_cmd = subparsers.add_parser("recall", help="Full agent recall")
    recall_cmd.add_argument("agent", help="Agent name")
    recall_cmd.add_argument("--query", help="Context query for cross-agent search")
    recall_cmd.add_argument("--top-k", type=int, default=5)
    recall_cmd.add_argument("--project-dir", default=".", help="Project root")

    # index
    index_cmd = subparsers.add_parser("index", help="Re-index memory files")
    index_cmd.add_argument("--project-dir", default=".", help="Project root")

    # read
    read_cmd = subparsers.add_parser("read", help="Read agent's full memory")
    read_cmd.add_argument("agent", help="Agent name")
    read_cmd.add_argument("--project-dir", default=".", help="Project root")

    # context
    context_cmd = subparsers.add_parser("context", help="Read project context")
    context_cmd.add_argument("--project-dir", default=".", help="Project root")

    args = parser.parse_args()

    if args.command == "setup":
        run_setup(args.project_dir)

    elif args.command == "status":
        show_status(args.project_dir)

    elif args.command == "save":
        path = save_memory(args.agent, args.content, args.project_dir)
        print(f"Saved to {path}")

    elif args.command == "search":
        results = search_memories(
            args.query, project_dir=args.project_dir,
            agent=args.agent, top_k=args.top_k,
        )
        if results:
            for r in results:
                print(f"\n--- [{r['agent']}] {r['heading']} (score: {r['score']}) ---")
                print(r["content"])
        else:
            print("No memories found.")

    elif args.command == "recall":
        result = recall_agent(
            args.agent, query=args.query,
            project_dir=args.project_dir, top_k=args.top_k,
        )
        print("=== OWN MEMORY ===")
        print(result["own_memory"] or "(no memory yet)")
        print("\n=== PROJECT CONTEXT ===")
        print(result["context"] or "(no context yet)")
        print("\n=== DECISIONS ===")
        print(result["decisions"] or "(no decisions yet)")
        if result["cross_agent"]:
            print("\n=== CROSS-AGENT CONTEXT ===")
            for r in result["cross_agent"]:
                print(f"\n--- [{r['agent']}] {r['heading']} (score: {r['score']}) ---")
                print(r["content"])

    elif args.command == "index":
        stats = index_memories(args.project_dir)
        if stats.get("skipped"):
            print("Skipped indexing — no embedding backend available. Using keyword search.")
            print("To enable: brew install ollama && ollama serve && ollama pull bge-m3")
        else:
            print(f"Indexed {stats['files']} files, {stats['chunks']} chunks")

    elif args.command == "read":
        content = read_memory(args.agent, args.project_dir)
        print(content or "(no memory yet)")

    elif args.command == "context":
        content = read_context(args.project_dir)
        print(content or "(no context yet)")


if __name__ == "__main__":
    main()
