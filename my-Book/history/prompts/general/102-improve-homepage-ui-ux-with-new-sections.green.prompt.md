--- 
id: 102
title: "Improve Homepage UI/UX with New Sections"
stage: green
date_iso: "2025-12-10"
surface: "agent"
model: "gemini-1.5-pro"
feature: "none"
branch: "main"
user: "unknown"
command: "unknown"
labels: ["docusaurus", "frontend", "css", "ui/ux", "homepage"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
 - "src/pages/index.tsx"
 - "src/pages/index.module.css"
tests_yaml:
 - "none"
---

# Improve Homepage UI/UX with New Sections

## PROMPT

You are an expert frontend UI/UX designer and Docusaurus customization engineer.

Your task is to improve ONLY the homepage (src/pages/index.tsx and index.module.css).  
Do NOT modify any other part of the site, including docs pages, navbar logic, sidebar, routes, or theme config.

========================
🎯 GOAL — HOMEPAGE IMPROVEMENT ONLY
========================

Make the homepage more beautiful, premium, and content-rich by applying the following changes:

1️⃣ Increase the logo size in the navbar (logo should be clearly visible and balanced).  
2️⃣ Keep the existing hero section but improve spacing, font size, visual balance.  
3️⃣ Add 2–3 new homepage sections under the hero banner, such as:
   - A feature grid (3–4 cards)
   - A module overview section (Module 1–4)
   - An elegant stats/impact section
   - Clean icons or minimal illustrations (no images required, just placeholders or styled divs)

4️⃣ Improve visual aesthetics:
   - Smooth spacing
   - Soft shadows
   - Rounded cards
   - Responsive alignment
   - Premium typography
   - Gradient accents matching the hero

5️⃣ Ensure the homepage looks modern like:
   - Vercel.com
   - Next.js homepage
   - OpenAI website
   - Stripe Docs landing section

6️⃣ DO NOT modify:
   - Docs layout
   - Sidebar
   - Routing
   - Any file other than index.tsx and index.module.css

========================
📂 FILES TO GENERATE CODE FOR
========================

1) src/pages/index.tsx  
   - Updated hero spacing  
   - Enlarged navbar logo support  
   - New homepage sections (feature grid + module overview + stats section)  

2) src/pages/index.module.css  
   - Styling for all homepage sections  
   - Improved layout, spacing, shadows  
   - Larger logo sizing class  
   - Premium modern UI components  

========================
🛠 REQUIRED OUTPUT FORMAT
========================

OUTPUT SECTION 1:  
Updated code for src/pages/index.tsx

OUTPUT SECTION 2:  
Updated code for src/pages/index.module.css

========================
⚠ RULES
========================

- DO NOT output explanations  
- DO NOT modify other files  
- DO NOT remove existing hero heading or button  
- Only beautify and add new sections  
- Only change homepage (index.tsx + index.module.css)  
- Keep code clean and production-ready  

========================
Now generate the updated homepage code.

## RESPONSE

**`src/pages/index.tsx`**
```tsx
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from './index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className={clsx('hero__title', styles.heroTitle)}>
          Physical AI & Humanoid Robotics
        </Heading>
        <p className={clsx('hero__subtitle', styles.heroSubtitle)}>
          A comprehensive guide exploring how AI-powered humanoid robots think, move, and interact with the physical world.
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/introduction/intro">
            Get Started →
          </Link>
        </div>
      </div>
    </header>
  );
}

const ValuePropList = [
    {
        title: 'Simulation First',
        icon: '💻',
        description:
            'Master digital twins and physics-based simulation to test, train, and validate robots in virtual environments before deploying to hardware.',
    },
    {
        title: 'Hands-On ROS2',
        icon: '🤖',
        description:
            'Go from zero to hero with the Robot Operating System (ROS2). Learn to build and manage complex robotics applications like a pro.',
    },
    {
        title: 'AI-Powered Perception',
        icon: '👁️',
        description:
            'Implement advanced perception systems using synthetic data and techniques like Visual SLAM for robust navigation and interaction.',
    },
];

const ModuleList = [
  {
    title: 'Module 1: ROS2 Foundations',
    description: 'Build a strong foundation in the Robot Operating System, the standard for modern robotics.',
    link: '/docs/introduction/intro',
  },
  {
    title: 'Module 2: Digital Twin & Simulation',
    description: 'Master Unity for physics-based simulation and sensor modeling.',
    link: '/docs/module-2-digital-twin/digital-twin-concept',
  },
  {
    title: 'Module 3: NVIDIA Isaac',
    description: 'Dive into advanced AI for robotics with NVIDIA\'s powerful tools for perception and navigation.',
    link: '/docs/module-3-nvidia-isaac/what-is-isaac',
  },
  {
    title: 'Module 4: Vision-Language Agents',
    description: 'Build a capstone project using cutting-edge VLAs for voice-to-action robot control.',
    link: '/docs/module-4-vla-capstone/capstone',
  },
];

const StatList = [
    {
        number: '04',
        label: 'Core Modules',
    },
    {
        number: '10+',
        label: 'Projects & Labs',
    },
    {
        number: '01',
        label: 'Capstone Project',
    },
];

function ValueProp({ title, icon, description }) {
    return (
        <div className={clsx('col col--4', styles.valueProp)}>
            <div className={clsx('card', styles.valuePropCard)}>
                <div className={styles.valuePropIcon}>{icon}</div>
                <div className="card__body">
                    <Heading as="h3" className={styles.valuePropTitle}>{title}</Heading>
                    <p>{description}</p>
                </div>
            </div>
        </div>
    );
}

function Module({ title, description, link }) {
  return (
    <Link to={link} className={styles.moduleLink}>
      <div className={clsx('card', styles.moduleCard)}>
          <div className="card__body">
              <Heading as="h3" className={styles.moduleTitle}>{title}</Heading>
              <p className={styles.moduleDescription}>{description}</p>
          </div>
      </div>
    </Link>
  );
}

function Stat({ number, label }) {
    return (
        <div className={clsx('col', styles.statItem)}>
            <div className={styles.statNumber}>{number}</div>
            <div className={styles.statLabel}>{label}</div>
        </div>
    );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`${siteConfig.title}`}
      description="A comprehensive guide exploring how AI-powered humanoid robots think, move, and interact with the physical world.">
      <HomepageHeader />
      <main className={styles.mainContent}>
        <section className={styles.section}>
            <div className="container">
                <div className="row">
                    {ValuePropList.map((props, idx) => (
                        <ValueProp key={idx} {...props} />
                    ))}
                </div>
            </div>
        </section>

        <section className={clsx(styles.section, styles.sectionAlt)}>
          <div className="container">
            <Heading as="h2" className={clsx('text--center', styles.sectionTitle)}>
              A Structured Learning Path
            </Heading>
            <p className={clsx('text--center', styles.sectionSubtitle)}>
                From fundamentals to advanced AI, our curriculum is designed to build your expertise step-by-step.
            </p>
            <div className={styles.moduleGrid}>
              {ModuleList.map((props, idx) => (
                <Module key={idx} {...props} />
              ))}
            </div>
          </div>
        </section>

        <section className={styles.section}>
            <div className="container">
                <div className={clsx('row', styles.statsContainer)}>
                    {StatList.map((props, idx) => (
                        <Stat key={idx} {...props} />
                    ))}
                </div>
            </div>
        </section>

      </main>
    </Layout>
  );
}
```

**`src/pages/index.module.css`**
```css
/* ========================================================================== 
   Global & Navbar
   ========================================================================== */
:global(.navbar__logo img) {
  height: 32px;
  width: auto;
  transition: transform 0.2s ease-in-out;
}

:global(.navbar__logo img:hover) {
  transform: scale(1.05);
}

/* ========================================================================== 
   Hero Section
   ========================================================================== */
.heroBanner {
  padding: 8rem 0 10rem;
  text-align: center;
  position: relative;
  overflow: hidden;
  background: linear-gradient(45deg, #5a78f0, #8d70e6);
  color: white;
}

.heroTitle {
  font-size: 4.5rem;
  font-weight: 800;
  line-height: 1.1;
  text-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.heroSubtitle {
  font-size: 1.5rem;
  font-weight: 300;
  max-width: 800px;
  margin: 2rem auto 2.5rem;
  opacity: 0.9;
}

.buttons .button {
  transition: all 0.2s ease-in-out;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  border: none;
}

.buttons .button:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.2);
}

/* ========================================================================== 
   Main Content & Sections
   ========================================================================== */
.mainContent {
  background-color: #fcfcff;
}

[data-theme='dark'] .mainContent {
  background-color: #0c0c10;
}

.section {
  padding: 6rem 0;
}

.sectionAlt {
  background-color: #ffffff;
}

[data-theme='dark'] .sectionAlt {
  background-color: #111115;
}

.sectionTitle {
  font-size: 2.5rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.sectionSubtitle {
  font-size: 1.2rem;
  max-width: 600px;
  margin-left: auto;
  margin-right: auto;
  margin-bottom: 4rem;
  color: var(--ifm-color-secondary-darkest);
}

[data-theme='dark'] .sectionSubtitle {
    color: var(--ifm-color-secondary-dark);
}

/* ========================================================================== 
   Value Props Section
   ========================================================================== */
.valueProp {
  margin-bottom: 2rem;
}

.valuePropCard {
  text-align: center;
  background-color: white;
  border: 1px solid #e9e9f2;
  border-radius: 12px;
  padding: 2rem 1.5rem;
  height: 100%;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

[data-theme='dark'] .valuePropCard {
  background-color: #16161c;
  border-color: #2a2a38;
}

.valuePropCard:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.07);
}

.valuePropIcon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: inline-block;
  padding: 0.8rem;
  border-radius: 50%;
  background: linear-gradient(45deg, rgba(90, 120, 240, 0.1), rgba(141, 112, 230, 0.1));
}

.valuePropTitle {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.75rem;
}

/* ========================================================================== 
   Module Overview Section
   ========================================================================== */
.moduleGrid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 1.5rem;
}

.moduleLink {
  text-decoration: none;
  color: inherit;
  transition: color 0.2s ease;
}

.moduleLink:hover {
  color: inherit;
  text-decoration: none;
}

.moduleCard {
  border-radius: 12px;
  border: 1px solid transparent;
  background-color: #f8f8fd;
  transition: all 0.3s ease;
  height: 100%;
}

[data-theme='dark'] .moduleCard {
  background-color: #1a1a21;
}

.moduleLink:hover .moduleCard {
  transform: translateY(-5px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  border-color: var(--ifm-color-primary-light);
}

.moduleTitle {
  font-size: 1.25rem;
  font-weight: 600;
  background: linear-gradient(45deg, var(--ifm-color-primary), var(--ifm-color-primary-dark));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}

[data-theme='dark'] .moduleTitle {
    background: linear-gradient(45deg, var(--ifm-color-primary-light), var(--ifm-color-primary-lighter));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.moduleDescription {
    margin-bottom: 0;
    color: var(--ifm-font-color-secondary);
}

/* ========================================================================== 
   Stats Section
   ========================================================================== */
.statsContainer {
  justify-content: center;
  gap: 4rem;
  text-align: center;
}

.statItem {
  padding: 0 1.5rem;
}

.statNumber {
  font-size: 3.5rem;
  font-weight: 800;
  line-height: 1;
  background: linear-gradient(45deg, #5a78f0, #8d70e6);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  margin-bottom: 0.5rem;
}

.statLabel {
  font-size: 1.1rem;
  font-weight: 500;
  color: var(--ifm-font-color-secondary);
}

/* ========================================================================== 
   Responsive Design
   ========================================================================== */
@media screen and (max-width: 996px) {
  .heroTitle {
    font-size: 3.5rem;
  }
  .heroSubtitle {
    font-size: 1.25rem;
  }
  .section {
    padding: 4rem 0;
  }
  .valueProp {
    margin-bottom: 1.5rem;
  }
}

@media screen and (max-width: 768px) {
  .heroTitle {
    font-size: 2.8rem;
  }
  .heroSubtitle {
    font-size: 1.1rem;
  }
  .moduleGrid {
    grid-template-columns: 1fr;
  }
  .statsContainer {
    flex-direction: column;
    gap: 2rem;
  }
}
```