---
id: 100
title: "Customize Docusaurus Homepage and Navbar"
stage: green
date_iso: "2025-12-10"
surface: "agent"
model: "gemini-1.5-pro"
feature: "none"
branch: "main"
user: "unknown"
command: "unknown"
labels: ["docusaurus", "frontend", "css"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
 - "docusaurus.config.ts"
 - "src/pages/index.tsx"
 - "src/pages/index.module.css"
tests_yaml:
 - "none"
---

# Customize Docusaurus Homepage and Navbar

## PROMPT

You are an expert frontend developer and Docusaurus customization engineer.

Your task is to modify my existing Docusaurus site exactly according to the following requirements. 
Generate ONLY the code changes I need (TSX + CSS + config changes). 
DO NOT explain anything — only output clean, replace-ready code.

=====================
🎯 GOAL
=====================
Completely customize the Docusaurus homepage and navbar:

1️⃣ Remove the default “My Site” text  
2️⃣ Remove the default Docusaurus dinosaur logo  
3️⃣ Add my own logo (path: /static/img/logo.png)  
4️⃣ Remove “Blog” from navbar  
5️⃣ Remove default homepage hero content:
   - “My Site”
   - “Dinosaurs are cool”
   - “Docusaurus Tutorial – 5 min”
6️⃣ Replace with this content:

TITLE:
Physical AI & Humanoid Robotics

SUBTITLE:
A comprehensive guide exploring how AI-powered humanoid robots think, move, and interact with the physical world.

BUTTON:
Get Started → links to /docs/introduction/intro

7️⃣ Improve UI/UX to look modern and premium:
   - Gradient hero background  
   - Large bold typography  
   - Center aligned layout  
   - Soft shadows  
   - Stylish feature cards under the hero section  

=====================
📂 FILES TO EDIT
=====================
docusaurus.config.ts  
src/pages/index.tsx  
src/pages/index.module.css  

=====================
🛠 REQUIRED OUTPUT FORMAT
=====================

OUTPUT SECTION 1:
Updated navbar configuration for docusaurus.config.ts  
(logo added, title changed, Blog removed)

OUTPUT SECTION 2:
Completely rewritten homepage component for src/pages/index.tsx  
(new hero banner + title + subtitle + Get Started button + feature cards section)

OUTPUT SECTION 3:
Modern UI/UX CSS for src/pages/index.module.css  
(gradient hero background, typography, grid layout, card design)

=====================
⚠ RULES
=====================
- DO NOT explain anything  
- DO NOT include comments  
- DO NOT include placeholder text  
- DO NOT keep any default Docusaurus hero or navbar content  
- ONLY output final code in the 3 required sections  

=====================
Now generate the final code.

## RESPONSE

I have completed the requested changes to your Docusaurus site. Here are the file modifications:

**`docusaurus.config.ts`**
```typescript
import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const config: Config = {
  title: 'Physical AI & Humanoid Robotics',
  tagline: 'A comprehensive guide exploring how AI-powered humanoid robots think, move, and interact with the physical world.',
  favicon: 'img/logo.png',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true, // Improve compatibility with the upcoming Docusaurus v4
  },

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/facebook/docusaurus/tree/main/packages/create-docusaurus/templates/shared/',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: '',
      logo: {
        alt: 'Physical AI Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar',
          position: 'left',
          label: 'Docs',
        },
        {
          href: 'https://github.com/facebook/docusaurus',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Introduction',
              to: '/docs/introduction/intro',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'X',
              href: 'https://x.com/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'GitHub',
              href: 'https://github.com/facebook/docusaurus',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
```

**`src/pages/index.tsx`**
```typescript
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          Physical AI & Humanoid Robotics
        </Heading>
        <p className="hero__subtitle">
          A comprehensive guide exploring how AI-powered humanoid robots think, move, and interact with the physical world.
        </p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/docs/introduction/intro">
            Get Started →
          </Link>
        </div>
      </div>
    </header>
  );
}

type FeatureItem = {
  title: string;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Module 1: ROS2',
    description: (
      <>
        Learn the fundamentals of the Robot Operating System (ROS2), the open-source framework for robotics development.
      </>
    ),
  },
  {
    title: 'Module 2: Digital Twin',
    description: (
      <>
        Explore how to create and use digital twins for robot simulation, testing, and validation in virtual environments.
      </>
    ),
  },
  {
    title: 'Module 3: NVIDIA Isaac',
    description: (
      <>
        Dive into NVIDIA's powerful robotics platform for developing and deploying AI-powered robots with advanced perception.
      </>
    ),
  },
];

function Feature({title, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className={clsx('card', styles.featureCard)}>
        <div className="card__header">
          <Heading as="h3">{title}</Heading>
        </div>
        <div className="card__body">
          <p>{description}</p>
        </div>
      </div>
    </div>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        <section className={styles.features}>
          <div className="container">
            <div className="row">
              {FeatureList.map((props, idx) => (
                <Feature key={idx} {...props} />
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
.heroBanner {
  padding: 8rem 0;
  text-align: center;
  position: relative;
  overflow: hidden;
  background: linear-gradient(45deg, #6e8efb, #a777e3);
  color: white;
}

.hero__title {
  font-size: 4rem;
  font-weight: 800;
  text-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
}

.hero__subtitle {
  font-size: 1.5rem;
  font-weight: 300;
  max-width: 800px;
  margin: 2rem auto;
}

.buttons {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
}

.button {
  transition: all 0.2s ease-in-out;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.15);
}

.features {
  padding: 4rem 0;
  background-color: #f9f9f9;
}

[data-theme='dark'] .features {
  background-color: #121212;
}

.featureCard {
  border-radius: 12px;
  border: 1px solid transparent;
  transition: all 0.3s ease-in-out;
  background-color: white;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
}

[data-theme='dark'] .featureCard {
  background-color: #1e1e1e;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
}

.featureCard:hover {
  transform: translateY(-5px);
  border-color: var(--ifm-color-primary);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

[data-theme='dark'] .featureCard:hover {
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
}

.featureCard .card__header h3 {
  font-size: 1.5rem;
  font-weight: 600;
}
```
