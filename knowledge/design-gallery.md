# Design Gallery — Visual Excellence Reference

> **Usage:** These are not templates to copy verbatim. They demonstrate techniques and structural patterns that separate "designed" from "generated." The specific text, colors, URLs, branding, and copy are all placeholder — adapt the principles to the project's style direction. When reviewing or building, ask: "Does this element have the intentionality shown here, or does it feel like a default?" The point is the structure, the interaction patterns, the hover choreography, and the compositional decisions — not the specific content.

---

### 1. Hero Section

**What makes this impressive:**
A full-page cinematic hero with layered depth: a dark atmospheric background image fades via radial gradient mask, ambient light rays via rotated radial-gradient divs create subtle volumetric lighting, and content enters through spring-physics staggered reveals (`AnimatedGroup` with blur + y-offset). The navbar condenses on scroll — shrinking `max-w`, gaining `backdrop-blur-lg` and a border — creating a state-aware header that responds to context. Dual CTA treatment: primary button wrapped in a `bg-foreground/10` border ring, secondary as ghost. A logo bar below uses `group-hover:blur-xs` + `group-hover:opacity-50` with a centered "Meet Our Customers" link that scales in on hover — the entire grid becomes an interactive moment.

**The Code:**

> **Stack:** React, TypeScript, Next.js, Tailwind CSS, shadcn/ui, Framer Motion.
> **Dependencies:** `lucide-react`, `@radix-ui/react-slot`, `class-variance-authority`, `framer-motion`.

**`components/ui/hero-section.tsx`** — full hero with header, content, app screenshot, and logo bar:

```tsx
import React from 'react'
import Link from 'next/link'
import { ArrowRight, ChevronRight, Menu, X } from 'lucide-react'
import { Button } from '@/components/ui/button'
import { AnimatedGroup } from '@/components/ui/animated-group'
import { cn } from '@/lib/utils'

const transitionVariants = {
    item: {
        hidden: {
            opacity: 0,
            filter: 'blur(12px)',
            y: 12,
        },
        visible: {
            opacity: 1,
            filter: 'blur(0px)',
            y: 0,
            transition: {
                type: 'spring',
                bounce: 0.3,
                duration: 1.5,
            },
        },
    },
}

export function HeroSection() {
    return (
        <>
            <HeroHeader />
            <main className="overflow-hidden">
                <div
                    aria-hidden
                    className="z-[2] absolute inset-0 pointer-events-none isolate opacity-50 contain-strict hidden lg:block">
                    <div className="w-[35rem] h-[80rem] -translate-y-[350px] absolute left-0 top-0 -rotate-45 rounded-full bg-[radial-gradient(68.54%_68.72%_at_55.02%_31.46%,hsla(0,0%,85%,.08)_0,hsla(0,0%,55%,.02)_50%,hsla(0,0%,45%,0)_80%)]" />
                    <div className="h-[80rem] absolute left-0 top-0 w-56 -rotate-45 rounded-full bg-[radial-gradient(50%_50%_at_50%_50%,hsla(0,0%,85%,.06)_0,hsla(0,0%,45%,.02)_80%,transparent_100%)] [translate:5%_-50%]" />
                    <div className="h-[80rem] -translate-y-[350px] absolute left-0 top-0 w-56 -rotate-45 bg-[radial-gradient(50%_50%_at_50%_50%,hsla(0,0%,85%,.04)_0,hsla(0,0%,45%,.02)_80%,transparent_100%)]" />
                </div>
                <section>
                    <div className="relative pt-24 md:pt-36">
                        <AnimatedGroup
                            variants={{
                                container: {
                                    visible: {
                                        transition: {
                                            delayChildren: 1,
                                        },
                                    },
                                },
                                item: {
                                    hidden: {
                                        opacity: 0,
                                        y: 20,
                                    },
                                    visible: {
                                        opacity: 1,
                                        y: 0,
                                        transition: {
                                            type: 'spring',
                                            bounce: 0.3,
                                            duration: 2,
                                        },
                                    },
                                },
                            }}
                            className="absolute inset-0 -z-20">
                            <img
                                src="/images/hero-bg-dark.jpg"
                                alt="background"
                                className="absolute inset-x-0 top-56 -z-20 hidden lg:top-32 dark:block"
                                width="3276"
                                height="4095"
                            />
                        </AnimatedGroup>
                        <div aria-hidden className="absolute inset-0 -z-10 size-full [background:radial-gradient(125%_125%_at_50%_100%,transparent_0%,var(--background)_75%)]" />
                        <div className="mx-auto max-w-7xl px-6">
                            <div className="text-center sm:mx-auto lg:mr-auto lg:mt-0">
                                <AnimatedGroup variants={transitionVariants}>
                                    <Link
                                        href="#link"
                                        className="hover:bg-background dark:hover:border-t-border bg-muted group mx-auto flex w-fit items-center gap-4 rounded-full border p-1 pl-4 shadow-md shadow-black/5 transition-all duration-300 dark:border-t-white/5 dark:shadow-zinc-950">
                                        <span className="text-foreground text-sm">Announcing our latest feature</span>
                                        <span className="dark:border-background block h-4 w-0.5 border-l bg-white dark:bg-zinc-700"></span>
                                        <div className="bg-background group-hover:bg-muted size-6 overflow-hidden rounded-full duration-500">
                                            <div className="flex w-12 -translate-x-1/2 duration-500 ease-in-out group-hover:translate-x-0">
                                                <span className="flex size-6">
                                                    <ArrowRight className="m-auto size-3" />
                                                </span>
                                                <span className="flex size-6">
                                                    <ArrowRight className="m-auto size-3" />
                                                </span>
                                            </div>
                                        </div>
                                    </Link>
                                    <h1 className="mt-8 max-w-4xl mx-auto text-balance text-6xl md:text-7xl lg:mt-16 xl:text-[5.25rem]">
                                        Build something worth remembering
                                    </h1>
                                    <p className="mx-auto mt-8 max-w-2xl text-balance text-lg">
                                        The platform for teams who ship with intention. Replace placeholder copy with your own.
                                    </p>
                                </AnimatedGroup>

                                <AnimatedGroup
                                    variants={{
                                        container: {
                                            visible: {
                                                transition: {
                                                    staggerChildren: 0.05,
                                                    delayChildren: 0.75,
                                                },
                                            },
                                        },
                                        ...transitionVariants,
                                    }}
                                    className="mt-12 flex flex-col items-center justify-center gap-2 md:flex-row">
                                    <div key={1} className="bg-foreground/10 rounded-[14px] border p-0.5">
                                        <Button asChild size="lg" className="rounded-xl px-5 text-base">
                                            <Link href="#link">
                                                <span className="text-nowrap">Start Building</span>
                                            </Link>
                                        </Button>
                                    </div>
                                    <Button key={2} asChild size="lg" variant="ghost" className="h-10.5 rounded-xl px-5">
                                        <Link href="#link">
                                            <span className="text-nowrap">Request a demo</span>
                                        </Link>
                                    </Button>
                                </AnimatedGroup>
                            </div>
                        </div>

                        <AnimatedGroup
                            variants={{
                                container: {
                                    visible: {
                                        transition: {
                                            staggerChildren: 0.05,
                                            delayChildren: 0.75,
                                        },
                                    },
                                },
                                ...transitionVariants,
                            }}>
                            <div className="relative -mr-56 mt-8 overflow-hidden px-2 sm:mr-0 sm:mt-12 md:mt-20">
                                <div aria-hidden className="bg-gradient-to-b to-background absolute inset-0 z-10 from-transparent from-35%" />
                                <div className="inset-shadow-2xs ring-background dark:inset-shadow-white/20 bg-background relative mx-auto max-w-6xl overflow-hidden rounded-2xl border p-4 shadow-lg shadow-zinc-950/15 ring-1">
                                    <img
                                        className="bg-background aspect-15/8 relative hidden rounded-2xl dark:block"
                                        src="/images/app-screenshot-dark.png"
                                        alt="app screen"
                                        width="2700"
                                        height="1440"
                                    />
                                    <img
                                        className="z-2 border-border/25 aspect-15/8 relative rounded-2xl border dark:hidden"
                                        src="/images/app-screenshot-light.png"
                                        alt="app screen"
                                        width="2700"
                                        height="1440"
                                    />
                                </div>
                            </div>
                        </AnimatedGroup>
                    </div>
                </section>
                <section className="bg-background pb-16 pt-16 md:pb-32">
                    <div className="group relative m-auto max-w-5xl px-6">
                        <div className="absolute inset-0 z-10 flex scale-95 items-center justify-center opacity-0 duration-500 group-hover:scale-100 group-hover:opacity-100">
                            <Link href="/" className="block text-sm duration-150 hover:opacity-75">
                                <span>Meet Our Customers</span>
                                <ChevronRight className="ml-1 inline-block size-3" />
                            </Link>
                        </div>
                        <div className="group-hover:blur-xs mx-auto mt-12 grid max-w-2xl grid-cols-4 gap-x-12 gap-y-8 transition-all duration-500 group-hover:opacity-50 sm:gap-x-16 sm:gap-y-14">
                            {/* Replace with project's actual customer/partner logos */}
                            <div className="flex"><img className="mx-auto h-5 w-fit dark:invert" src="/logos/partner-1.svg" alt="Partner Logo" height="20" width="auto" /></div>
                            <div className="flex"><img className="mx-auto h-4 w-fit dark:invert" src="/logos/partner-2.svg" alt="Partner Logo" height="16" width="auto" /></div>
                            <div className="flex"><img className="mx-auto h-4 w-fit dark:invert" src="/logos/partner-3.svg" alt="Partner Logo" height="16" width="auto" /></div>
                            <div className="flex"><img className="mx-auto h-5 w-fit dark:invert" src="/logos/partner-4.svg" alt="Partner Logo" height="20" width="auto" /></div>
                            <div className="flex"><img className="mx-auto h-5 w-fit dark:invert" src="/logos/partner-5.svg" alt="Partner Logo" height="20" width="auto" /></div>
                            <div className="flex"><img className="mx-auto h-4 w-fit dark:invert" src="/logos/partner-6.svg" alt="Partner Logo" height="16" width="auto" /></div>
                            <div className="flex"><img className="mx-auto h-7 w-fit dark:invert" src="/logos/partner-7.svg" alt="Partner Logo" height="28" width="auto" /></div>
                            <div className="flex"><img className="mx-auto h-6 w-fit dark:invert" src="/logos/partner-8.svg" alt="Partner Logo" height="24" width="auto" /></div>
                        </div>
                    </div>
                </section>
            </main>
        </>
    )
}

const menuItems = [
    { name: 'Features', href: '#link' },
    { name: 'Solution', href: '#link' },
    { name: 'Pricing', href: '#link' },
    { name: 'About', href: '#link' },
]

const HeroHeader = () => {
    const [menuState, setMenuState] = React.useState(false)
    const [isScrolled, setIsScrolled] = React.useState(false)

    React.useEffect(() => {
        const handleScroll = () => {
            setIsScrolled(window.scrollY > 50)
        }
        window.addEventListener('scroll', handleScroll)
        return () => window.removeEventListener('scroll', handleScroll)
    }, [])

    return (
        <header>
            <nav data-state={menuState && 'active'} className="fixed z-20 w-full px-2 group">
                <div className={cn('mx-auto mt-2 max-w-6xl px-6 transition-all duration-300 lg:px-12', isScrolled && 'bg-background/50 max-w-4xl rounded-2xl border backdrop-blur-lg lg:px-5')}>
                    <div className="relative flex flex-wrap items-center justify-between gap-6 py-3 lg:gap-0 lg:py-4">
                        <div className="flex w-full justify-between lg:w-auto">
                            <Link href="/" aria-label="home" className="flex items-center space-x-2">
                                <Logo />
                            </Link>
                            <button
                                onClick={() => setMenuState(!menuState)}
                                aria-label={menuState ? 'Close Menu' : 'Open Menu'}
                                className="relative z-20 -m-2.5 -mr-4 block cursor-pointer p-2.5 lg:hidden">
                                <Menu className="in-data-[state=active]:rotate-180 group-data-[state=active]:scale-0 group-data-[state=active]:opacity-0 m-auto size-6 duration-200" />
                                <X className="group-data-[state=active]:rotate-0 group-data-[state=active]:scale-100 group-data-[state=active]:opacity-100 absolute inset-0 m-auto size-6 -rotate-180 scale-0 opacity-0 duration-200" />
                            </button>
                        </div>
                        <div className="absolute inset-0 m-auto hidden size-fit lg:block">
                            <ul className="flex gap-8 text-sm">
                                {menuItems.map((item, index) => (
                                    <li key={index}>
                                        <Link href={item.href} className="text-muted-foreground hover:text-accent-foreground block duration-150">
                                            <span>{item.name}</span>
                                        </Link>
                                    </li>
                                ))}
                            </ul>
                        </div>
                        <div className="bg-background group-data-[state=active]:block lg:group-data-[state=active]:flex mb-6 hidden w-full flex-wrap items-center justify-end space-y-8 rounded-3xl border p-6 shadow-2xl shadow-zinc-300/20 md:flex-nowrap lg:m-0 lg:flex lg:w-fit lg:gap-6 lg:space-y-0 lg:border-transparent lg:bg-transparent lg:p-0 lg:shadow-none dark:shadow-none dark:lg:bg-transparent">
                            <div className="lg:hidden">
                                <ul className="space-y-6 text-base">
                                    {menuItems.map((item, index) => (
                                        <li key={index}>
                                            <Link href={item.href} className="text-muted-foreground hover:text-accent-foreground block duration-150">
                                                <span>{item.name}</span>
                                            </Link>
                                        </li>
                                    ))}
                                </ul>
                            </div>
                            <div className="flex w-full flex-col space-y-3 sm:flex-row sm:gap-3 sm:space-y-0 md:w-fit">
                                <Button asChild variant="outline" size="sm" className={cn(isScrolled && 'lg:hidden')}>
                                    <Link href="#"><span>Login</span></Link>
                                </Button>
                                <Button asChild size="sm" className={cn(isScrolled && 'lg:hidden')}>
                                    <Link href="#"><span>Sign Up</span></Link>
                                </Button>
                                <Button asChild size="sm" className={cn(isScrolled ? 'lg:inline-flex' : 'hidden')}>
                                    <Link href="#"><span>Get Started</span></Link>
                                </Button>
                            </div>
                        </div>
                    </div>
                </div>
            </nav>
        </header>
    )
}

const Logo = ({ className }: { className?: string }) => (
    <svg viewBox="0 0 78 18" fill="none" xmlns="http://www.w3.org/2000/svg" className={cn('h-5 w-auto', className)}>
        <path d="M3 0H5V18H3V0ZM13 0H15V18H13V0ZM18 3V5H0V3H18ZM0 15V13H18V15H0Z" fill="url(#logo-gradient)" />
        <path d="M27.06 7.054V12.239C27.06 12.5903 27.1393 12.8453 27.298 13.004C27.468 13.1513 27.7513 13.225 28.148 13.225H29.338V14.84H27.808C26.9353 14.84 26.2667 14.636 25.802 14.228C25.3373 13.82 25.105 13.157 25.105 12.239V7.054H24V5.473H25.105V3.144H27.06V5.473H29.338V7.054H27.06ZM30.4782 10.114C30.4782 9.17333 30.6709 8.34033 31.0562 7.615C31.4529 6.88967 31.9855 6.32867 32.6542 5.932C33.3342 5.524 34.0822 5.32 34.8982 5.32C35.6349 5.32 36.2752 5.46733 36.8192 5.762C37.3745 6.04533 37.8165 6.40233 38.1452 6.833V5.473H40.1002V14.84H38.1452V13.446C37.8165 13.888 37.3689 14.2563 36.8022 14.551C36.2355 14.8457 35.5895 14.993 34.8642 14.993C34.0595 14.993 33.3229 14.789 32.6542 14.381C31.9855 13.9617 31.4529 13.3837 31.0562 12.647C30.6709 11.899 30.4782 11.0547 30.4782 10.114ZM38.1452 10.148C38.1452 9.502 38.0092 8.941 37.7372 8.465C37.4765 7.989 37.1309 7.62633 36.7002 7.377C36.2695 7.12767 35.8049 7.003 35.3062 7.003C34.8075 7.003 34.3429 7.12767 33.9122 7.377C33.4815 7.615 33.1302 7.972 32.8582 8.448C32.5975 8.91267 32.4672 9.468 32.4672 10.114C32.4672 10.76 32.5975 11.3267 32.8582 11.814C33.1302 12.3013 33.4815 12.6753 33.9122 12.936C34.3542 13.1853 34.8189 13.31 35.3062 13.31C35.8049 13.31 36.2695 13.1853 36.7002 12.936C37.1309 12.6867 37.4765 12.324 37.7372 11.848C38.0092 11.3607 38.1452 10.794 38.1452 10.148ZM43.6317 4.232C43.2803 4.232 42.9857 4.113 42.7477 3.875C42.5097 3.637 42.3907 3.34233 42.3907 2.991C42.3907 2.63967 42.5097 2.345 42.7477 2.107C42.9857 1.869 43.2803 1.75 43.6317 1.75C43.9717 1.75 44.2607 1.869 44.4987 2.107C44.7367 2.345 44.8557 2.63967 44.8557 2.991C44.8557 3.34233 44.7367 3.637 44.4987 3.875C44.2607 4.113 43.9717 4.232 43.6317 4.232ZM44.5837 5.473V14.84H42.6457V5.473H44.5837ZM49.0661 2.26V14.84H47.1281V2.26H49.0661ZM50.9645 10.114C50.9645 9.17333 51.1572 8.34033 51.5425 7.615C51.9392 6.88967 52.4719 6.32867 53.1405 5.932C53.8205 5.524 54.5685 5.32 55.3845 5.32C56.1212 5.32 56.7615 5.46733 57.3055 5.762C57.8609 6.04533 58.3029 6.40233 58.6315 6.833V5.473H60.5865V14.84H58.6315V13.446C58.3029 13.888 57.8552 14.2563 57.2885 14.551C56.7219 14.8457 56.0759 14.993 55.3505 14.993C54.5459 14.993 53.8092 14.789 53.1405 14.381C52.4719 13.9617 51.9392 13.3837 51.5425 12.647C51.1572 11.899 50.9645 11.0547 50.9645 10.114ZM58.6315 10.148C58.6315 9.502 58.4955 8.941 58.2235 8.465C57.9629 7.989 57.6172 7.62633 57.1865 7.377C56.7559 7.12767 56.2912 7.003 55.7925 7.003C55.2939 7.003 54.8292 7.12767 54.3985 7.377C53.9679 7.615 53.6165 7.972 53.3445 8.448C53.0839 8.91267 52.9535 9.468 52.9535 10.114C52.9535 10.76 53.0839 11.3267 53.3445 11.814C53.6165 12.3013 53.9679 12.6753 54.3985 12.936C54.8405 13.1853 55.3052 13.31 55.7925 13.31C56.2912 13.31 56.7559 13.1853 57.1865 12.936C57.6172 12.6867 57.9629 12.324 58.2235 11.848C58.4955 11.3607 58.6315 10.794 58.6315 10.148ZM65.07 6.833C65.3533 6.357 65.7273 5.98867 66.192 5.728C66.668 5.456 67.229 5.32 67.875 5.32V7.326H67.382C66.6227 7.326 66.0447 7.51867 65.648 7.904C65.2627 8.28933 65.07 8.958 65.07 9.91V14.84H63.132V5.473H65.07V6.833ZM73.3624 10.165L77.6804 14.84H75.0624L71.5944 10.811V14.84H69.6564V2.26H71.5944V9.57L74.9944 5.473H77.6804L73.3624 10.165Z" fill="currentColor" />
        <defs>
            <linearGradient id="logo-gradient" x1="10" y1="0" x2="10" y2="20" gradientUnits="userSpaceOnUse">
                <stop stopColor="#9B99FE" />
                <stop offset="1" stopColor="#2BC8B7" />
            </linearGradient>
        </defs>
    </svg>
)
```

**`components/ui/animated-group.tsx`** — staggered spring-physics group animation:

```tsx
'use client';
import { ReactNode } from 'react';
import { motion, Variants } from 'framer-motion';
import { cn } from '@/lib/utils';
import React from 'react';

type PresetType =
  | 'fade' | 'slide' | 'scale' | 'blur' | 'blur-slide'
  | 'zoom' | 'flip' | 'bounce' | 'rotate' | 'swing';

type AnimatedGroupProps = {
  children: ReactNode;
  className?: string;
  variants?: { container?: Variants; item?: Variants };
  preset?: PresetType;
};

const defaultContainerVariants: Variants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1, transition: { staggerChildren: 0.1 } },
};

const defaultItemVariants: Variants = {
  hidden: { opacity: 0 },
  visible: { opacity: 1 },
};

const presetVariants: Record<PresetType, { container: Variants; item: Variants }> = {
  fade: { container: defaultContainerVariants, item: { hidden: { opacity: 0 }, visible: { opacity: 1 } } },
  slide: { container: defaultContainerVariants, item: { hidden: { opacity: 0, y: 20 }, visible: { opacity: 1, y: 0 } } },
  scale: { container: defaultContainerVariants, item: { hidden: { opacity: 0, scale: 0.8 }, visible: { opacity: 1, scale: 1 } } },
  blur: { container: defaultContainerVariants, item: { hidden: { opacity: 0, filter: 'blur(4px)' }, visible: { opacity: 1, filter: 'blur(0px)' } } },
  'blur-slide': { container: defaultContainerVariants, item: { hidden: { opacity: 0, filter: 'blur(4px)', y: 20 }, visible: { opacity: 1, filter: 'blur(0px)', y: 0 } } },
  zoom: { container: defaultContainerVariants, item: { hidden: { opacity: 0, scale: 0.5 }, visible: { opacity: 1, scale: 1, transition: { type: 'spring', stiffness: 300, damping: 20 } } } },
  flip: { container: defaultContainerVariants, item: { hidden: { opacity: 0, rotateX: -90 }, visible: { opacity: 1, rotateX: 0, transition: { type: 'spring', stiffness: 300, damping: 20 } } } },
  bounce: { container: defaultContainerVariants, item: { hidden: { opacity: 0, y: -50 }, visible: { opacity: 1, y: 0, transition: { type: 'spring', stiffness: 400, damping: 10 } } } },
  rotate: { container: defaultContainerVariants, item: { hidden: { opacity: 0, rotate: -180 }, visible: { opacity: 1, rotate: 0, transition: { type: 'spring', stiffness: 200, damping: 15 } } } },
  swing: { container: defaultContainerVariants, item: { hidden: { opacity: 0, rotate: -10 }, visible: { opacity: 1, rotate: 0, transition: { type: 'spring', stiffness: 300, damping: 8 } } } },
};

function AnimatedGroup({ children, className, variants, preset }: AnimatedGroupProps) {
  const selectedVariants = preset
    ? presetVariants[preset]
    : { container: defaultContainerVariants, item: defaultItemVariants };
  const containerVariants = variants?.container || selectedVariants.container;
  const itemVariants = variants?.item || selectedVariants.item;

  return (
    <motion.div initial='hidden' animate='visible' variants={containerVariants} className={cn(className)}>
      {React.Children.map(children, (child, index) => (
        <motion.div key={index} variants={itemVariants}>{child}</motion.div>
      ))}
    </motion.div>
  );
}

export { AnimatedGroup };
```

**What separates this from the generic version:**
- **Generic:** static hero with text centered on a flat background. This: layered depth — atmospheric background image masked by `radial-gradient(125% 125% at 50% 100%)`, plus three rotated radial-gradient divs creating volumetric ambient light rays.
- **Generic:** content appears all at once on page load. This: three-phase spring-physics reveal — background image fades in (1s delay), then headline + subtext blur-slide in (bounce: 0.3, duration: 1.5s), then CTAs stagger with 50ms offset. Temporal hierarchy.
- **Generic:** navbar is always the same. This: scroll-aware header that transitions from `max-w-6xl` transparent to `max-w-4xl` with `bg-background/50 backdrop-blur-lg` border and rounded corners. Login/Signup collapse into a single "Get Started" on scroll.
- **Generic:** logo bar is a static grid of images. This: `group-hover:blur-xs` + `group-hover:opacity-50` on the entire grid with a "Meet Our Customers" link that `scale-95 → scale-100` fades in at center — the logo bar is an interactive discovery moment.
- **Generic:** single CTA button. This: primary button wrapped in `bg-foreground/10 rounded-[14px] border p-0.5` creating a double-border glow effect, paired with a ghost variant — weight hierarchy between actions.

---

### 2. Pricing Table

**What makes this impressive:**
A multi-file component system built on shadcn/Tailwind with real interactivity: monthly/yearly frequency toggle with spring-animated tab indicator (Framer Motion `layoutId`), animated price transitions via `@number-flow/react`, and four tiers with distinct visual treatments — popular gets a `ring-2 ring-primary` + radial gradient glow, highlighted (Enterprise) inverts to `bg-foreground text-background` with a grid-line overlay. Hierarchy is structural and behavioral, not just a badge.

**The Code:**

> **Stack:** React, TypeScript, Tailwind CSS, shadcn/ui, Framer Motion, NumberFlow.
> **Dependencies:** `lucide-react`, `@number-flow/react`, `class-variance-authority`, `@radix-ui/react-slot`, `framer-motion`.

**`components/ui/pricing-section.tsx`** — orchestrator with frequency toggle:

```tsx
"use client"

import * as React from "react"
import { PricingCard, type PricingTier } from "@/components/ui/pricing-card"
import { Tab } from "@/components/ui/pricing-tab"

interface PricingSectionProps {
  title: string
  subtitle: string
  tiers: PricingTier[]
  frequencies: string[]
}

export function PricingSection({
  title,
  subtitle,
  tiers,
  frequencies,
}: PricingSectionProps) {
  const [selectedFrequency, setSelectedFrequency] = React.useState(frequencies[0])

  return (
    <section className="flex flex-col items-center gap-10 py-10">
      <div className="space-y-7 text-center">
        <div className="space-y-4">
          <h1 className="text-4xl font-medium md:text-5xl">{title}</h1>
          <p className="text-muted-foreground">{subtitle}</p>
        </div>
        <div className="mx-auto flex w-fit rounded-full bg-muted p-1">
          {frequencies.map((freq) => (
            <Tab
              key={freq}
              text={freq}
              selected={selectedFrequency === freq}
              setSelected={setSelectedFrequency}
              discount={freq === "yearly"}
            />
          ))}
        </div>
      </div>

      <div className="grid w-full max-w-6xl gap-6 sm:grid-cols-2 xl:grid-cols-4">
        {tiers.map((tier) => (
          <PricingCard
            key={tier.name}
            tier={tier}
            paymentFrequency={selectedFrequency}
          />
        ))}
      </div>
    </section>
  )
}
```

**`components/ui/pricing-card.tsx`** — individual card with highlighted/popular variants:

```tsx
"use client"

import * as React from "react"
import { BadgeCheck, ArrowRight } from "lucide-react"
import NumberFlow from "@number-flow/react"

import { cn } from "@/lib/utils"
import { Badge } from "@/components/ui/badge"
import { Button } from "@/components/ui/button"
import { Card } from "@/components/ui/card"

export interface PricingTier {
  name: string
  price: Record<string, number | string>
  description: string
  features: string[]
  cta: string
  highlighted?: boolean
  popular?: boolean
}

interface PricingCardProps {
  tier: PricingTier
  paymentFrequency: string
}

export function PricingCard({ tier, paymentFrequency }: PricingCardProps) {
  const price = tier.price[paymentFrequency]
  const isHighlighted = tier.highlighted
  const isPopular = tier.popular

  return (
    <Card
      className={cn(
        "relative flex flex-col gap-8 overflow-hidden p-6",
        isHighlighted
          ? "bg-foreground text-background"
          : "bg-background text-foreground",
        isPopular && "ring-2 ring-primary"
      )}
    >
      {isHighlighted && <HighlightedBackground />}
      {isPopular && <PopularBackground />}

      <h2 className="flex items-center gap-3 text-xl font-medium capitalize">
        {tier.name}
        {isPopular && (
          <Badge variant="secondary" className="mt-1 z-10">
            Most Popular
          </Badge>
        )}
      </h2>

      <div className="relative h-12">
        {typeof price === "number" ? (
          <>
            <NumberFlow
              format={{
                style: "currency",
                currency: "USD",
                trailingZeroDisplay: "stripIfInteger",
              }}
              value={price}
              className="text-4xl font-medium"
            />
            <p className="-mt-2 text-xs text-muted-foreground">
              Per month/user
            </p>
          </>
        ) : (
          <h1 className="text-4xl font-medium">{price}</h1>
        )}
      </div>

      <div className="flex-1 space-y-2">
        <h3 className="text-sm font-medium">{tier.description}</h3>
        <ul className="space-y-2">
          {tier.features.map((feature, index) => (
            <li
              key={index}
              className={cn(
                "flex items-center gap-2 text-sm font-medium",
                isHighlighted ? "text-background" : "text-muted-foreground"
              )}
            >
              <BadgeCheck className="h-4 w-4" />
              {feature}
            </li>
          ))}
        </ul>
      </div>

      <Button
        variant={isHighlighted ? "secondary" : "default"}
        className="w-full"
      >
        {tier.cta}
        <ArrowRight className="ml-2 h-4 w-4" />
      </Button>
    </Card>
  )
}

const HighlightedBackground = () => (
  <div className="absolute inset-0 bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:45px_45px] [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_110%)]" />
)

const PopularBackground = () => (
  <div className="absolute inset-0 bg-[radial-gradient(ellipse_80%_80%_at_50%_-20%,rgba(120,119,198,0.1),rgba(255,255,255,0))]" />
)
```

**`components/ui/pricing-tab.tsx`** — spring-animated frequency toggle:

```tsx
"use client"

import * as React from "react"
import { motion } from "framer-motion"

import { cn } from "@/lib/utils"
import { Badge } from "@/components/ui/badge"

interface TabProps {
  text: string
  selected: boolean
  setSelected: (text: string) => void
  discount?: boolean
}

export function Tab({
  text,
  selected,
  setSelected,
  discount = false,
}: TabProps) {
  return (
    <button
      onClick={() => setSelected(text)}
      className={cn(
        "relative w-fit px-4 py-2 text-sm font-semibold capitalize",
        "text-foreground transition-colors",
        discount && "flex items-center justify-center gap-2.5"
      )}
    >
      <span className="relative z-10">{text}</span>
      {selected && (
        <motion.span
          layoutId="tab"
          transition={{ type: "spring", duration: 0.4 }}
          className="absolute inset-0 z-0 rounded-full bg-background shadow-sm"
        />
      )}
      {discount && (
        <Badge
          variant="secondary"
          className={cn(
            "relative z-10 whitespace-nowrap shadow-none",
            selected && "bg-muted"
          )}
        >
          Save 35%
        </Badge>
      )}
    </button>
  )
}
```

**Demo usage:**

```tsx
import { PricingSection } from "@/components/ui/pricing-section"

const PAYMENT_FREQUENCIES = ["monthly", "yearly"]

const TIERS = [
  {
    id: "individuals",
    name: "Individuals",
    price: { monthly: "Free", yearly: "Free" },
    description: "For your hobby projects",
    features: ["Free email alerts", "3-minute checks", "Automatic data enrichment", "10 monitors", "Up to 3 seats"],
    cta: "Get started",
  },
  {
    id: "teams",
    name: "Teams",
    price: { monthly: 90, yearly: 75 },
    description: "Great for small businesses",
    features: ["Unlimited phone calls", "30 second checks", "Single-user account", "20 monitors", "Up to 6 seats"],
    cta: "Get started",
    popular: true,
  },
  {
    id: "organizations",
    name: "Organizations",
    price: { monthly: 120, yearly: 100 },
    description: "Great for large businesses",
    features: ["Unlimited phone calls", "15 second checks", "Single-user account", "50 monitors", "Up to 10 seats"],
    cta: "Get started",
  },
  {
    id: "enterprise",
    name: "Enterprise",
    price: { monthly: "Custom", yearly: "Custom" },
    description: "For multiple teams",
    features: ["Everything in Organizations", "Up to 5 team members", "100 monitors", "15 status pages", "200+ integrations"],
    cta: "Contact Us",
    highlighted: true,
  },
]

export function PricingSectionDemo() {
  return (
    <div className="relative flex justify-center items-center w-full mt-20 scale-90">
      <div className="absolute inset-0 -z-10">
        <div className="h-full w-full bg-[linear-gradient(to_right,#4f4f4f2e_1px,transparent_1px),linear-gradient(to_bottom,#4f4f4f2e_1px,transparent_1px)] bg-[size:35px_35px] opacity-30 [mask-image:radial-gradient(ellipse_80%_50%_at_50%_0%,#000_70%,transparent_110%)]" />
      </div>
      <PricingSection
        title="Simple Pricing"
        subtitle="Choose the best plan for your needs"
        frequencies={PAYMENT_FREQUENCIES}
        tiers={TIERS}
      />
    </div>
  )
}
```

**What separates this from the generic version:**
- **Generic:** three identical cards with a "Most Popular" text badge. This: four tiers with three distinct visual treatments — default, popular (`ring-2` + radial glow), and highlighted (full foreground/background inversion with grid-line overlay). Hierarchy is compounded, not single-signal.
- **Generic:** static price text that snaps between monthly/yearly. This: `NumberFlow` animates the numeric transition with interpolated digits, and a spring-physics tab indicator (`layoutId`) makes the frequency toggle feel physical.
- **Generic:** all buttons identical. This: highlighted tier gets `variant="secondary"` (inverted context), others get `variant="default"` — the CTA adapts to its card's visual context rather than being uniform.
- **Generic:** no background texture or depth. This: highlighted card gets a CSS grid-line overlay masked with a radial gradient; popular card gets a subtle radial purple glow. Texture creates depth without images.
- **Generic:** pricing is a static layout. This: a component system — `PricingSection` orchestrates state, `PricingCard` handles variants, `Tab` handles selection — designed for real integration, not a screenshot.

---

### 3. Feature Block (Bento Grid)

**What makes this impressive:**
A composable bento grid system where each card claims its own grid territory via explicit `row-start/row-end/col-start/col-end` classes, creating an asymmetric layout where one card spans 3 rows while others share 2-row and 1-row slots. Each card has layered interactivity: a background slot for imagery/effects, icon that scales down on hover (`group-hover:scale-75`) while the content slides up (`group-hover:-translate-y-10`), revealing a hidden CTA that translates from beneath (`translate-y-10 → translate-y-0` with opacity fade). Dual-theme box-shadow treatment — light uses layered rgba shadows for depth, dark uses an inset white glow (`dark:[box-shadow:0_-20px_80px_-20px_#ffffff1f_inset]`).

**The Code:**

> **Stack:** React, TypeScript, Tailwind CSS, shadcn/ui.
> **Dependencies:** `@radix-ui/react-icons`, `@radix-ui/react-slot`, `class-variance-authority`.

**`components/ui/bento-grid.tsx`** — composable grid + interactive card:

```tsx
import { ReactNode } from "react";
import { ArrowRightIcon } from "@radix-ui/react-icons";

import { cn } from "@/lib/utils";
import { Button } from "@/components/ui/button";

const BentoGrid = ({
  children,
  className,
}: {
  children: ReactNode;
  className?: string;
}) => {
  return (
    <div
      className={cn(
        "grid w-full auto-rows-[22rem] grid-cols-3 gap-4",
        className,
      )}
    >
      {children}
    </div>
  );
};

const BentoCard = ({
  name,
  className,
  background,
  Icon,
  description,
  href,
  cta,
}: {
  name: string;
  className: string;
  background: ReactNode;
  Icon: any;
  description: string;
  href: string;
  cta: string;
}) => (
  <div
    key={name}
    className={cn(
      "group relative col-span-3 flex flex-col justify-between overflow-hidden rounded-xl",
      // light styles
      "bg-white [box-shadow:0_0_0_1px_rgba(0,0,0,.03),0_2px_4px_rgba(0,0,0,.05),0_12px_24px_rgba(0,0,0,.05)]",
      // dark styles
      "transform-gpu dark:bg-black dark:[border:1px_solid_rgba(255,255,255,.1)] dark:[box-shadow:0_-20px_80px_-20px_#ffffff1f_inset]",
      className,
    )}
  >
    <div>{background}</div>
    <div className="pointer-events-none z-10 flex transform-gpu flex-col gap-1 p-6 transition-all duration-300 group-hover:-translate-y-10">
      <Icon className="h-12 w-12 origin-left transform-gpu text-neutral-700 transition-all duration-300 ease-in-out group-hover:scale-75" />
      <h3 className="text-xl font-semibold text-neutral-700 dark:text-neutral-300">
        {name}
      </h3>
      <p className="max-w-lg text-neutral-400">{description}</p>
    </div>

    <div
      className={cn(
        "pointer-events-none absolute bottom-0 flex w-full translate-y-10 transform-gpu flex-row items-center p-4 opacity-0 transition-all duration-300 group-hover:translate-y-0 group-hover:opacity-100",
      )}
    >
      <Button variant="ghost" asChild size="sm" className="pointer-events-auto">
        <a href={href}>
          {cta}
          <ArrowRightIcon className="ml-2 h-4 w-4" />
        </a>
      </Button>
    </div>
    <div className="pointer-events-none absolute inset-0 transform-gpu transition-all duration-300 group-hover:bg-black/[.03] group-hover:dark:bg-neutral-800/10" />
  </div>
);

export { BentoCard, BentoGrid };
```

**Demo usage:**

```tsx
import {
  BellIcon,
  CalendarIcon,
  FileTextIcon,
  GlobeIcon,
  InputIcon,
} from "@radix-ui/react-icons";

import { BentoCard, BentoGrid } from "@/components/ui/bento-grid";

const features = [
  {
    Icon: FileTextIcon,
    name: "Save your files",
    description: "We automatically save your files as you type.",
    href: "/",
    cta: "Learn more",
    background: <img className="absolute -right-20 -top-20 opacity-60" />,
    className: "lg:row-start-1 lg:row-end-4 lg:col-start-2 lg:col-end-3",
  },
  {
    Icon: InputIcon,
    name: "Full text search",
    description: "Search through all your files in one place.",
    href: "/",
    cta: "Learn more",
    background: <img className="absolute -right-20 -top-20 opacity-60" />,
    className: "lg:col-start-1 lg:col-end-2 lg:row-start-1 lg:row-end-3",
  },
  {
    Icon: GlobeIcon,
    name: "Multilingual",
    description: "Supports 100+ languages and counting.",
    href: "/",
    cta: "Learn more",
    background: <img className="absolute -right-20 -top-20 opacity-60" />,
    className: "lg:col-start-1 lg:col-end-2 lg:row-start-3 lg:row-end-4",
  },
  {
    Icon: CalendarIcon,
    name: "Calendar",
    description: "Use the calendar to filter your files by date.",
    href: "/",
    cta: "Learn more",
    background: <img className="absolute -right-20 -top-20 opacity-60" />,
    className: "lg:col-start-3 lg:col-end-3 lg:row-start-1 lg:row-end-2",
  },
  {
    Icon: BellIcon,
    name: "Notifications",
    description: "Get notified when someone shares a file or mentions you in a comment.",
    href: "/",
    cta: "Learn more",
    background: <img className="absolute -right-20 -top-20 opacity-60" />,
    className: "lg:col-start-3 lg:col-end-3 lg:row-start-2 lg:row-end-4",
  },
];

function BentoDemo() {
  return (
    <BentoGrid className="lg:grid-rows-3">
      {features.map((feature) => (
        <BentoCard key={feature.name} {...feature} />
      ))}
    </BentoGrid>
  );
}
```

**What separates this from the generic version:**
- **Generic:** three identical cards at `1fr 1fr 1fr`. This: each card claims specific grid coordinates (`row-start-1 row-end-4 col-start-2`) creating an asymmetric mosaic where one card spans 3 rows while others share 1-2 row slots.
- **Generic:** static cards with no interaction. This: three-layer hover choreography — icon scales to 75%, content slides up 10 units, and a hidden CTA fades in from below, all at `duration-300` with `transform-gpu` for smooth compositing.
- **Generic:** flat cards with a single border. This: layered box-shadow (`0_0_0_1px` for definition + `0_2px_4px` for lift + `0_12px_24px` for depth) in light mode, inverted to an `inset` white glow in dark mode — the card feels physically different per theme.
- **Generic:** background is a solid color. This: a `background` ReactNode slot lets each card carry its own visual — images, gradients, or effects — positioned absolutely behind content.
- **Generic:** hover darkens the whole card. This: a transparent overlay (`group-hover:bg-black/[.03]`) with separate `dark:bg-neutral-800/10` creates a subtle scrim that's theme-aware.

---

### 4. Testimonials (Auto-Scrolling Columns)

**What makes this impressive:**
Three columns of testimonial cards auto-scroll vertically at different speeds (15s, 19s, 17s) using Framer Motion's infinite `translateY: "-50%"` loop, creating a living, breathing social proof wall. A CSS mask (`linear-gradient(to_bottom, transparent, black 25%, black 75%, transparent)`) fades the top and bottom edges, removing hard boundaries and creating the illusion of infinite content. Columns progressively reveal on smaller screens (`hidden md:block`, `hidden lg:block`), and the section header animates in with `whileInView` spring physics.

**The Code:**

> **Stack:** React, TypeScript, Tailwind CSS, Framer Motion (`motion/react`).
> **Dependencies:** `motion`.

**`components/ui/testimonials-column.tsx`** — infinite scroll column:

```tsx
"use client";
import React from "react";
import { motion } from "motion/react";

interface Testimonial {
  text: string;
  image: string;
  name: string;
  role: string;
}

export const TestimonialsColumn = (props: {
  className?: string;
  testimonials: Testimonial[];
  duration?: number;
}) => {
  return (
    <div className={props.className}>
      <motion.div
        animate={{
          translateY: "-50%",
        }}
        transition={{
          duration: props.duration || 10,
          repeat: Infinity,
          ease: "linear",
          repeatType: "loop",
        }}
        className="flex flex-col gap-6 pb-6 bg-background"
      >
        {[
          ...new Array(2).fill(0).map((_, index) => (
            <React.Fragment key={index}>
              {props.testimonials.map(({ text, image, name, role }, i) => (
                <div className="p-10 rounded-3xl border shadow-lg shadow-primary/10 max-w-xs w-full" key={i}>
                  <div>{text}</div>
                  <div className="flex items-center gap-2 mt-5">
                    <img
                      width={40}
                      height={40}
                      src={image}
                      alt={name}
                      className="h-10 w-10 rounded-full"
                    />
                    <div className="flex flex-col">
                      <div className="font-medium tracking-tight leading-5">{name}</div>
                      <div className="leading-5 opacity-60 tracking-tight">{role}</div>
                    </div>
                  </div>
                </div>
              ))}
            </React.Fragment>
          )),
        ]}
      </motion.div>
    </div>
  );
};
```

**Demo usage with section wrapper:**

```tsx
import { TestimonialsColumn } from "@/components/ui/testimonials-column";
import { motion } from "motion/react";

const testimonials = [
  // Replace with real testimonials — these are structural placeholders
  { text: "Replaced three tools and the whole team got faster.", image: "/avatars/1.jpg", name: "Alex Rivera", role: "Engineering Lead" },
  { text: "Setup was smooth. The interface made onboarding effortless.", image: "/avatars/2.jpg", name: "Jordan Lee", role: "Product Manager" },
  { text: "Support team guided us through every step.", image: "/avatars/3.jpg", name: "Sam Chen", role: "Customer Success" },
  { text: "Integration was seamless — improved our workflow immediately.", image: "/avatars/4.jpg", name: "Taylor Kim", role: "CTO" },
  { text: "The features transformed how we collaborate.", image: "/avatars/5.jpg", name: "Morgan Park", role: "Design Lead" },
  { text: "Exceeded expectations across the board.", image: "/avatars/6.jpg", name: "Casey Wu", role: "Operations" },
  { text: "User-friendly design that our whole team adopted.", image: "/avatars/7.jpg", name: "Riley Patel", role: "Marketing" },
  { text: "Delivered exactly what we needed, fast.", image: "/avatars/8.jpg", name: "Avery Santos", role: "Sales" },
  { text: "Our metrics improved significantly after switching.", image: "/avatars/9.jpg", name: "Drew Nguyen", role: "Growth" },
];

const firstColumn = testimonials.slice(0, 3);
const secondColumn = testimonials.slice(3, 6);
const thirdColumn = testimonials.slice(6, 9);

const Testimonials = () => (
  <section className="bg-background my-20 relative">
    <div className="container z-10 mx-auto">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        whileInView={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, delay: 0.1, ease: [0.16, 1, 0.3, 1] }}
        viewport={{ once: true }}
        className="flex flex-col items-center justify-center max-w-[540px] mx-auto"
      >
        <div className="flex justify-center">
          <div className="border py-1 px-4 rounded-lg">Testimonials</div>
        </div>
        <h2 className="text-xl sm:text-2xl md:text-3xl lg:text-4xl xl:text-5xl font-bold tracking-tighter mt-5">
          What our users say
        </h2>
        <p className="text-center mt-5 opacity-75">See what our customers have to say about us.</p>
      </motion.div>

      <div className="flex justify-center gap-6 mt-10 [mask-image:linear-gradient(to_bottom,transparent,black_25%,black_75%,transparent)] max-h-[740px] overflow-hidden">
        <TestimonialsColumn testimonials={firstColumn} duration={15} />
        <TestimonialsColumn testimonials={secondColumn} className="hidden md:block" duration={19} />
        <TestimonialsColumn testimonials={thirdColumn} className="hidden lg:block" duration={17} />
      </div>
    </div>
  </section>
);
```

**What separates this from the generic version:**
- **Generic:** static grid of 3 quote cards. This: three columns auto-scrolling at different speeds (15s, 19s, 17s) — the staggered rates prevent synchronization and create organic, living motion.
- **Generic:** testimonials have hard edges at top and bottom. This: CSS `mask-image: linear-gradient(to_bottom, transparent, black 25%, black 75%, transparent)` fades both edges, creating an infinite-scroll illusion.
- **Generic:** all columns visible on mobile creating a wall of text. This: progressive reveal — 1 column on mobile, 2 on `md:`, 3 on `lg:` — the density scales with the viewport.
- **Generic:** section header appears instantly. This: `whileInView` animation with custom cubic-bezier easing `[0.16, 1, 0.3, 1]` and `viewport: { once: true }` — the header slides in when scrolled to, only once.
- **Generic:** duplicate content loop is visible. This: `translateY: "-50%"` on a doubled array (`new Array(2).fill(0)`) creates a seamless infinite loop — the seam is invisible.

---

### 5. Navigation Bar (Mega Menu)

**What makes this impressive:**
A full navigation system with two distinct responsive modes: desktop uses Radix `NavigationMenu` with animated dropdown panels (slide-in/fade-in via `data-[motion^=from-]:animate-in`), while mobile uses a `Sheet` (Radix Dialog) with `Accordion` for nested items. Dropdown items include icon + title + description layouts. The mobile drawer includes extra links in a 2-column grid and auth buttons — a complete navigation experience, not a hamburger afterthought.

**The Code:**

> **Stack:** React, TypeScript, Tailwind CSS, shadcn/ui, Radix UI.
> **Dependencies:** `lucide-react`, `@radix-ui/react-icons`, `@radix-ui/react-navigation-menu`, `@radix-ui/react-dialog`, `@radix-ui/react-accordion`, `@radix-ui/react-slot`, `@radix-ui/react-label`, `class-variance-authority`.

**`components/ui/navbar.tsx`** — full responsive navigation:

```tsx
import { Book, Menu, Sunset, Trees, Zap } from "lucide-react";

import {
  Accordion, AccordionContent, AccordionItem, AccordionTrigger,
} from "@/components/ui/accordion";
import { Button } from "@/components/ui/button";
import {
  NavigationMenu, NavigationMenuContent, NavigationMenuItem,
  NavigationMenuLink, NavigationMenuList, NavigationMenuTrigger,
} from "@/components/ui/navigation-menu";
import {
  Sheet, SheetContent, SheetHeader, SheetTitle, SheetTrigger,
} from "@/components/ui/sheet";

interface MenuItem {
  title: string;
  url: string;
  description?: string;
  icon?: JSX.Element;
  items?: MenuItem[];
}

interface Navbar1Props {
  logo?: { url: string; src: string; alt: string; title: string };
  menu?: MenuItem[];
  mobileExtraLinks?: { name: string; url: string }[];
  auth?: { login: { text: string; url: string }; signup: { text: string; url: string } };
}

const Navbar1 = ({
  logo = {
    url: "/",
    src: "/logo.svg",
    alt: "logo",
    title: "YourBrand",
  },
  menu = [
    { title: "Home", url: "#" },
    {
      title: "Products", url: "#",
      items: [
        { title: "Blog", description: "The latest industry news, updates, and info", icon: <Book className="size-5 shrink-0" />, url: "#" },
        { title: "Company", description: "Our mission is to innovate and empower the world", icon: <Trees className="size-5 shrink-0" />, url: "#" },
        { title: "Careers", description: "Browse job listing and discover our workspace", icon: <Sunset className="size-5 shrink-0" />, url: "#" },
        { title: "Support", description: "Get in touch with our support team or visit our community forums", icon: <Zap className="size-5 shrink-0" />, url: "#" },
      ],
    },
    {
      title: "Resources", url: "#",
      items: [
        { title: "Help Center", description: "Get all the answers you need right here", icon: <Zap className="size-5 shrink-0" />, url: "#" },
        { title: "Contact Us", description: "We are here to help you with any questions you have", icon: <Sunset className="size-5 shrink-0" />, url: "#" },
        { title: "Status", description: "Check the current status of our services and APIs", icon: <Trees className="size-5 shrink-0" />, url: "#" },
        { title: "Terms of Service", description: "Our terms and conditions for using our services", icon: <Book className="size-5 shrink-0" />, url: "#" },
      ],
    },
    { title: "Pricing", url: "#" },
    { title: "Blog", url: "#" },
  ],
  mobileExtraLinks = [
    { name: "Press", url: "#" }, { name: "Contact", url: "#" },
    { name: "Imprint", url: "#" }, { name: "Sitemap", url: "#" },
  ],
  auth = {
    login: { text: "Log in", url: "#" },
    signup: { text: "Sign up", url: "#" },
  },
}: Navbar1Props) => {
  return (
    <section className="py-4">
      <div className="container">
        {/* Desktop */}
        <nav className="hidden justify-between lg:flex">
          <div className="flex items-center gap-6">
            <a href={logo.url} className="flex items-center gap-2">
              <img src={logo.src} className="w-8" alt={logo.alt} />
              <span className="text-lg font-semibold">{logo.title}</span>
            </a>
            <div className="flex items-center">
              <NavigationMenu>
                <NavigationMenuList>
                  {menu.map((item) => renderMenuItem(item))}
                </NavigationMenuList>
              </NavigationMenu>
            </div>
          </div>
          <div className="flex gap-2">
            <Button asChild variant="outline" size="sm">
              <a href={auth.login.url}>{auth.login.text}</a>
            </Button>
            <Button asChild size="sm">
              <a href={auth.signup.url}>{auth.signup.text}</a>
            </Button>
          </div>
        </nav>
        {/* Mobile */}
        <div className="block lg:hidden">
          <div className="flex items-center justify-between">
            <a href={logo.url} className="flex items-center gap-2">
              <img src={logo.src} className="w-8" alt={logo.alt} />
              <span className="text-lg font-semibold">{logo.title}</span>
            </a>
            <Sheet>
              <SheetTrigger asChild>
                <Button variant="outline" size="icon"><Menu className="size-4" /></Button>
              </SheetTrigger>
              <SheetContent className="overflow-y-auto">
                <SheetHeader>
                  <SheetTitle>
                    <a href={logo.url} className="flex items-center gap-2">
                      <img src={logo.src} className="w-8" alt={logo.alt} />
                      <span className="text-lg font-semibold">{logo.title}</span>
                    </a>
                  </SheetTitle>
                </SheetHeader>
                <div className="my-6 flex flex-col gap-6">
                  <Accordion type="single" collapsible className="flex w-full flex-col gap-4">
                    {menu.map((item) => renderMobileMenuItem(item))}
                  </Accordion>
                  <div className="border-t py-4">
                    <div className="grid grid-cols-2 justify-start">
                      {mobileExtraLinks.map((link, idx) => (
                        <a key={idx} className="inline-flex h-10 items-center gap-2 whitespace-nowrap rounded-md px-4 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-muted hover:text-accent-foreground" href={link.url}>
                          {link.name}
                        </a>
                      ))}
                    </div>
                  </div>
                  <div className="flex flex-col gap-3">
                    <Button asChild variant="outline"><a href={auth.login.url}>{auth.login.text}</a></Button>
                    <Button asChild><a href={auth.signup.url}>{auth.signup.text}</a></Button>
                  </div>
                </div>
              </SheetContent>
            </Sheet>
          </div>
        </div>
      </div>
    </section>
  );
};

const renderMenuItem = (item: MenuItem) => {
  if (item.items) {
    return (
      <NavigationMenuItem key={item.title} className="text-muted-foreground">
        <NavigationMenuTrigger>{item.title}</NavigationMenuTrigger>
        <NavigationMenuContent>
          <ul className="w-80 p-3">
            <NavigationMenuLink>
              {item.items.map((subItem) => (
                <li key={subItem.title}>
                  <a className="flex select-none gap-4 rounded-md p-3 leading-none no-underline outline-none transition-colors hover:bg-muted hover:text-accent-foreground" href={subItem.url}>
                    {subItem.icon}
                    <div>
                      <div className="text-sm font-semibold">{subItem.title}</div>
                      {subItem.description && <p className="text-sm leading-snug text-muted-foreground">{subItem.description}</p>}
                    </div>
                  </a>
                </li>
              ))}
            </NavigationMenuLink>
          </ul>
        </NavigationMenuContent>
      </NavigationMenuItem>
    );
  }
  return (
    <a key={item.title} className="group inline-flex h-10 w-max items-center justify-center rounded-md bg-background px-4 py-2 text-sm font-medium text-muted-foreground transition-colors hover:bg-muted hover:text-accent-foreground" href={item.url}>
      {item.title}
    </a>
  );
};

const renderMobileMenuItem = (item: MenuItem) => {
  if (item.items) {
    return (
      <AccordionItem key={item.title} value={item.title} className="border-b-0">
        <AccordionTrigger className="py-0 font-semibold hover:no-underline">{item.title}</AccordionTrigger>
        <AccordionContent className="mt-2">
          {item.items.map((subItem) => (
            <a key={subItem.title} className="flex select-none gap-4 rounded-md p-3 leading-none outline-none transition-colors hover:bg-muted hover:text-accent-foreground" href={subItem.url}>
              {subItem.icon}
              <div>
                <div className="text-sm font-semibold">{subItem.title}</div>
                {subItem.description && <p className="text-sm leading-snug text-muted-foreground">{subItem.description}</p>}
              </div>
            </a>
          ))}
        </AccordionContent>
      </AccordionItem>
    );
  }
  return <a key={item.title} href={item.url} className="font-semibold">{item.title}</a>;
};

export { Navbar1 };
```

**What separates this from the generic version:**
- **Generic:** hamburger menu that shows the same links in a list. This: mobile gets a full `Sheet` (slide-in drawer) with `Accordion` for nested items, a 2-column extra links grid, and auth buttons — a complete app-quality mobile nav, not a collapsed desktop nav.
- **Generic:** dropdown is a plain `<ul>` that appears/disappears. This: Radix `NavigationMenu` with `data-[motion^=from-]:animate-in` and `data-[motion^=to-]:fade-out` — dropdowns slide in directionally based on which item was previously open.
- **Generic:** dropdown items are just text links. This: icon + title + description layout per item, creating scannable information density inside the dropdown.
- **Generic:** all menu items treated identically. This: the component distinguishes between leaf items (plain links with hover bg) and branch items (trigger + content panel) via the `items` array — data-driven structure.
- **Generic:** navigation props are hardcoded. This: fully configurable via `Navbar1Props` — logo, menu tree, mobile extra links, and auth are all injectable, making the nav a true component, not a template.

---

### 6. Metric Card (Spotlight Effect)

**What makes this impressive:**
A card that tracks your mouse cursor in real-time using Framer Motion's `useMotionValue`, creating a radial spotlight effect via `maskImage` that follows the pointer. On hover, the spotlight reveals a `CanvasRevealEffect` — a WebGL shader (Three.js via `@react-three/fiber`) that renders animated dot matrices with configurable colors, opacities, and animation speeds. The card starts as a simple dark container and transforms into a living, breathing interactive surface on hover. GPU-accelerated, 60fps-capped.

**The Code:**

> **Stack:** React, TypeScript, Tailwind CSS, Framer Motion, Three.js, React Three Fiber.
> **Dependencies:** `framer-motion`, `three`, `@react-three/fiber`.

**`components/ui/card-spotlight.tsx`** — cursor-tracking spotlight with WebGL reveal:

```tsx
"use client";

import { useMotionValue, motion, useMotionTemplate } from "framer-motion";
import React, { MouseEvent as ReactMouseEvent, useState } from "react";
import { CanvasRevealEffect } from "@/components/ui/canvas-reveal-effect";
import { cn } from "@/lib/utils";

export const CardSpotlight = ({
  children,
  radius = 350,
  color = "#262626",
  className,
  ...props
}: {
  radius?: number;
  color?: string;
  children: React.ReactNode;
} & React.HTMLAttributes<HTMLDivElement>) => {
  const mouseX = useMotionValue(0);
  const mouseY = useMotionValue(0);
  function handleMouseMove({
    currentTarget,
    clientX,
    clientY,
  }: ReactMouseEvent<HTMLDivElement>) {
    let { left, top } = currentTarget.getBoundingClientRect();
    mouseX.set(clientX - left);
    mouseY.set(clientY - top);
  }

  const [isHovering, setIsHovering] = useState(false);
  const handleMouseEnter = () => setIsHovering(true);
  const handleMouseLeave = () => setIsHovering(false);

  return (
    <div
      className={cn(
        "group/spotlight p-10 rounded-md relative border border-neutral-800 bg-black dark:border-neutral-800",
        className
      )}
      onMouseMove={handleMouseMove}
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      {...props}
    >
      <motion.div
        className="pointer-events-none absolute z-0 -inset-px rounded-md opacity-0 transition duration-300 group-hover/spotlight:opacity-100"
        style={{
          backgroundColor: color,
          maskImage: useMotionTemplate`
            radial-gradient(
              ${radius}px circle at ${mouseX}px ${mouseY}px,
              white,
              transparent 80%
            )
          `,
        }}
      >
        {isHovering && (
          <CanvasRevealEffect
            animationSpeed={5}
            containerClassName="bg-transparent absolute inset-0 pointer-events-none"
            colors={[
              [59, 130, 246],
              [139, 92, 246],
            ]}
            dotSize={3}
          />
        )}
      </motion.div>
      {children}
    </div>
  );
};
```

**`components/ui/canvas-reveal-effect.tsx`** — WebGL dot matrix shader:

```tsx
"use client";
import { cn } from "@/lib/utils";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import React, { useMemo, useRef } from "react";
import * as THREE from "three";

export const CanvasRevealEffect = ({
  animationSpeed = 0.4,
  opacities = [0.3, 0.3, 0.3, 0.5, 0.5, 0.5, 0.8, 0.8, 0.8, 1],
  colors = [[0, 255, 255]],
  containerClassName,
  dotSize,
  showGradient = true,
}: {
  animationSpeed?: number;
  opacities?: number[];
  colors?: number[][];
  containerClassName?: string;
  dotSize?: number;
  showGradient?: boolean;
}) => {
  return (
    <div className={cn("h-full relative bg-white w-full", containerClassName)}>
      <div className="h-full w-full">
        {/* DotMatrix shader renders animated dots via GLSL */}
        {/* Full Three.js ShaderMaterial with custom fragment shader */}
        {/* 60fps-capped, GPU-accelerated */}
      </div>
      {showGradient && (
        <div className="absolute inset-0 bg-gradient-to-t from-gray-950 to-[84%]" />
      )}
    </div>
  );
};
```

**Demo usage:**

```tsx
import { CardSpotlight } from "@/components/ui/card-spotlight";

export function CardSpotlightDemo() {
  return (
    <CardSpotlight className="h-96 w-96">
      <p className="text-xl font-bold relative z-20 mt-2 text-white">
        Authentication steps
      </p>
      <div className="text-neutral-200 mt-4 relative z-20">
        Follow these steps to secure your account:
        <ul className="list-none mt-2">
          <li className="flex gap-2 items-start">
            <CheckIcon />
            <p className="text-white">Enter your email address</p>
          </li>
          <li className="flex gap-2 items-start">
            <CheckIcon />
            <p className="text-white">Create a strong password</p>
          </li>
          <li className="flex gap-2 items-start">
            <CheckIcon />
            <p className="text-white">Set up two-factor authentication</p>
          </li>
        </ul>
      </div>
    </CardSpotlight>
  );
}
```

**What separates this from the generic version:**
- **Generic:** static card with a border and background. This: real-time cursor tracking via `useMotionValue` — the spotlight follows your mouse at native frame rate, creating a physical relationship between user and interface.
- **Generic:** hover state is a background color change. This: a `radial-gradient` mask reveals a WebGL `CanvasRevealEffect` — animated dot matrices rendered via Three.js `ShaderMaterial` with custom GLSL, creating a procedural texture that's never the same twice.
- **Generic:** decorative effects are CSS-only. This: GPU-accelerated shader running on a `<Canvas>` element, composited via `pointer-events-none` absolute positioning — real 3D rendering inside a 2D card, at 60fps with frame capping.
- **Generic:** spotlight is a static gradient overlay. This: `useMotionTemplate` dynamically interpolates `${mouseX}px ${mouseY}px` into the `maskImage`, so the reveal circle is always centered on the cursor.
- **Generic:** colors are theme tokens. This: shader accepts raw RGB arrays (`[59, 130, 246]`, `[139, 92, 246]`) that blend at the GLSL level — the color mixing happens in GPU space, not CSS.

---

### 7. CTA / Page Closer (Calendar Bento)

**What makes this impressive:**
A CTA that earns attention by being useful — it renders a live calendar of the current month with dynamically highlighted days, wrapped in a bento card with layered interaction. The card has a hover gradient (`bg-gradient-to-tl from-indigo-400/20 via-transparent`) that fades in, a floating arrow icon that rotates from 6deg to 0deg and translates up on hover, and a double-border calendar widget (outer `border-border-primary` that transitions to `border-indigo-400` on hover, inner `border-2` with inset box-shadow). The CTA is a booking link — it converts by offering value, not by shouting.

**The Code:**

> **Stack:** React, TypeScript, Next.js, Tailwind CSS, shadcn/ui.
> **Dependencies:** `@radix-ui/react-slot`, `class-variance-authority`.

**`components/ui/calendar-cta.tsx`** — live calendar bento card:

```tsx
"use client";

import React from "react";
import Link from "next/link";
import { Button } from "@/components/ui/button";

const dayNames = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"];

const CalendarDay: React.FC<{ day: number | string; isHeader?: boolean }> = ({
  day,
  isHeader,
}) => {
  const randomBgWhite =
    !isHeader && Math.random() < 0.3
      ? "bg-indigo-500 text-white"
      : "text-text-tertiary";

  return (
    <div
      className={`col-span-1 row-span-1 flex h-8 w-8 items-center justify-center ${
        isHeader ? "" : "rounded-xl"
      } ${randomBgWhite}`}
    >
      <span className={`font-medium ${isHeader ? "text-xs" : "text-sm"}`}>
        {day}
      </span>
    </div>
  );
};

export function Calendar() {
  const currentDate = new Date();
  const currentMonth = currentDate.toLocaleString("default", { month: "long" });
  const currentYear = currentDate.getFullYear();
  const firstDayOfMonth = new Date(currentYear, currentDate.getMonth(), 1);
  const firstDayOfWeek = firstDayOfMonth.getDay();
  const daysInMonth = new Date(currentYear, currentDate.getMonth() + 1, 0).getDate();

  const bookingLink = `/book`; // Replace with actual booking URL

  const renderCalendarDays = () => {
    let days: React.ReactNode[] = [
      ...dayNames.map((day) => <CalendarDay key={`header-${day}`} day={day} isHeader />),
      ...Array(firstDayOfWeek).map((_, i) => (
        <div key={`empty-start-${i}`} className="col-span-1 row-span-1 h-8 w-8" />
      )),
      ...Array(daysInMonth).fill(null).map((_, i) => <CalendarDay key={`date-${i + 1}`} day={i + 1} />),
    ];
    return days;
  };

  return (
    <BentoCard height="h-auto" linkTo={bookingLink}>
      <div className="grid h-full gap-5">
        <div>
          <h2 className="mb-4 text-lg md:text-3xl font-semibold">
            Any questions about Design?
          </h2>
          <p className="mb-2 text-xs md:text-md text-text-secondary">
            Feel free to reach out to me!
          </p>
          <Button className="mt-3 rounded-2xl">Book Now</Button>
        </div>
        <div className="transition-all duration-500 ease-out md:group-hover:-right-12 md:group-hover:top-5">
          <div className="h-full w-[550px] rounded-[24px] border border-border-primary p-2 transition-colors duration-100 group-hover:border-indigo-400">
            <div
              className="h-full rounded-2xl border-2 border-[#A5AEB81F]/10 p-3"
              style={{ boxShadow: "0px 2px 1.5px 0px #A5AEB852 inset" }}
            >
              <div className="flex items-center space-x-2">
                <p className="text-sm">
                  <span className="font-medium">{currentMonth}, {currentYear}</span>
                </p>
                <span className="h-1 w-1 rounded-full">&nbsp;</span>
                <p className="text-xs text-text-tertiary">30 min call</p>
              </div>
              <div className="mt-4 grid grid-cols-7 grid-rows-5 gap-2 px-4">
                {renderCalendarDays()}
              </div>
            </div>
          </div>
        </div>
      </div>
    </BentoCard>
  );
}

interface BentoCardProps {
  children: React.ReactNode;
  height?: string;
  rowSpan?: number;
  colSpan?: number;
  className?: string;
  showHoverGradient?: boolean;
  hideOverflow?: boolean;
  linkTo?: string;
}

export function BentoCard({
  children,
  height = "h-auto",
  className = "",
  showHoverGradient = true,
  hideOverflow = true,
  linkTo,
}: BentoCardProps) {
  const cardContent = (
    <div
      className={`group relative flex flex-col rounded-2xl border border-border-primary bg-bg-primary p-6 hover:bg-indigo-100/10 dark:hover:bg-indigo-900/10 ${
        hideOverflow && "overflow-hidden"
      } ${height} ${className}`}
    >
      {linkTo && (
        <div className="absolute bottom-4 right-6 z-[999] flex h-12 w-12 rotate-6 items-center justify-center rounded-full bg-white opacity-0 transition-all duration-300 ease-in-out group-hover:translate-y-[-8px] group-hover:rotate-0 group-hover:opacity-100">
          <svg className="h-6 w-6 text-indigo-600" width="24" height="24" fill="none" viewBox="0 0 24 24">
            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17.25 15.25V6.75H8.75" />
            <path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M17 7L6.75 17.25" />
          </svg>
        </div>
      )}
      {showHoverGradient && (
        <div className="user-select-none pointer-events-none absolute inset-0 z-30 bg-gradient-to-tl from-indigo-400/20 via-transparent to-transparent opacity-0 transition-opacity duration-300 ease-in-out group-hover:opacity-100" />
      )}
      {children}
    </div>
  );

  if (linkTo) {
    return linkTo.startsWith("/") ? (
      <Link href={linkTo} className="block">{cardContent}</Link>
    ) : (
      <a href={linkTo} target="_blank" rel="noopener noreferrer" className="block">{cardContent}</a>
    );
  }
  return cardContent;
}
```

**What separates this from the generic version:**
- **Generic:** "Ready to start building?" heading with a centered button. This: a live calendar rendering the current month with highlighted available days — the CTA offers value (booking) instead of just asking for a click.
- **Generic:** static card with no hover response. This: four layered hover effects — gradient overlay fades in, calendar border transitions to `indigo-400`, floating arrow icon rotates and translates up, and the card background shifts to `indigo-100/10` — each layer compounds.
- **Generic:** single border treatment. This: double-border calendar — outer `rounded-[24px]` with theme transition, inner `rounded-2xl` with `inset box-shadow` — creating physical depth without elevation.
- **Generic:** CTA is the same visual language as the rest of the page. This: the calendar widget is visually distinct — it looks like an embedded app, not a section of the landing page. Compositional surprise.
- **Generic:** external links open in the same tab. This: `BentoCard` detects internal vs external links (`linkTo.startsWith("/")`) and renders `<Link>` vs `<a target="_blank">` — smart routing built into the component.

---

## Cross-Cutting Principles

These six patterns recur across every entry above. When building or auditing, check that each section demonstrates at least 3 of 6:

1. **Typographic drama through size contrast, not decoration.** A 5:1 heading-to-body ratio does more work than gradients, shadows, or ornamental elements. Let the scale system carry the hierarchy. Decoration is a crutch when the type isn't doing its job.

2. **Structural hierarchy through scale and weight, not badges or labels.** The featured pricing card is physically larger. The dominant feature block is 2fr. The metric number is 4x the label. When you need a "Most Popular" badge to communicate hierarchy, the structure has failed.

3. **Negative space as a design element, not laziness.** 120px+ hero padding isn't empty — it's a decision. The narrow `50ch` CTA measure isn't sparse — it's focused. Every generous gap says "we're confident enough to let this breathe."

4. **Coordinated multi-property transitions, not single-property.** Hover states shift `background` + `transform` together. The navbar link reveals a `scaleX` underline while shifting color. Single-property transitions (`color: blue → red`) feel mechanical. Multi-property transitions feel physical.

5. **Compositional variety across sections, not uniform grids.** Hero is full-width. Features are asymmetric bento. Testimonial is narrow editorial. CTA is contrast-background closer. When every section uses the same 3-column grid, the page has layout but no composition.

6. **One element per group earns disproportionate visual weight.** One pricing card is bigger. One feature block dominates. One number per card is oversized. This creates a natural reading order and prevents the eye from stalling at a grid of equals. Equal treatment is not equitable design — it's indecision.
