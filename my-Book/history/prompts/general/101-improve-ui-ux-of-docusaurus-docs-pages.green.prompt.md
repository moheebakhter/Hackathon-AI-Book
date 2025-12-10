---
id: 101
title: "Improve UI/UX of Docusaurus Docs Pages"
stage: green
date_iso: "2025-12-10"
surface: "agent"
model: "gemini-1.5-pro"
feature: "none"
branch: "main"
user: "unknown"
command: "unknown"
labels: ["docusaurus", "frontend", "css", "ui/ux"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
 - "src/css/custom.css"
 - "src/theme/DocItem/index.tsx"
 - "src/theme/DocItem/styles.module.css"
tests_yaml:
 - "none"
---

# Improve UI/UX of Docusaurus Docs Pages

## PROMPT

You are an expert Docusaurus UI/UX customization engineer.

Your task is to generate ONLY the code required to improve the UI/UX inside the documentation pages ("docs pages") so that they visually match the modern, clean, premium style of my homepage.

IMPORTANT:
❗ Do NOT modify anything except the internal docs page UI and typography.
❗ Do NOT change navbar, homepage, hero section, sidebars, routing, or configuration.
❗ Only output clean replace-ready CSS and component overrides—NO explanations.

========================
🎯 GOAL (DO EXACTLY THIS)
========================

Apply the following improvements ONLY inside documentation pages:

1️⃣ Center the main H1 heading on docs pages  
2️⃣ Improve readability: increase spacing, clean typography  
3️⃣ Set a max-width for content (similar to premium docs like Vercel/Stripe)  
4️⃣ Add a soft card-style background behind the documentation content  
5️⃣ Add slight glassmorphism effect with subtle shadows  
6️⃣ Make dark-mode styles match the new look  
7️⃣ DO NOT modify homepage UI  
8️⃣ DO NOT modify sidebar content, only sidebar hover styling  
9️⃣ Breadcrumbs should have a modern clean look  

========================
📂 FILES TO GENERATE CODE FOR
========================

1) src/css/custom.css  
   - Global docs page styling  
   - Typography  
   - Card background  
   - Spacing  
   - Sidebar hover effect  
   - Breadcrumbs UI  

2) src/theme/DocItem/index.tsx  
   - Wrapper for docs page  
   - Optional class wrapper (NO layout changes beyond docs content area)

3) src/theme/DocItem/styles.module.css  
   - Styling for improved H1 heading  
   - Gradient heading style  
   - Matching homepage visual tone  

========================
🛠 REQUIRED OUTPUT FORMAT
========================

OUTPUT SECTION 1:  
Code for src/css/custom.css

OUTPUT SECTION 2:  
Code for src/theme/DocItem/index.tsx

OUTPUT SECTION 3:  
Code for src/theme/DocItem/styles.module.css

========================
⚠ RULES
========================

- Do NOT output explanations  
- Do NOT modify any other files  
- Do NOT touch homepage  
- Do NOT touch navbar or config  
- Do NOT add new components beyond what is required  
- ONLY output final code in the 3 sections  

========================
Now generate the code exactly as requested.

## RESPONSE

**`src/css/custom.css`**
```css
/**
 * Any CSS placed here will be applied to the whole site,
 * affecting both the homepage and docs pages.
 *
 * For styles specific to docs pages, use selectors that
 * target elements within the documentation layout.
 */

/* ==========================================================================
   Docs Page - Main Content Container
   ========================================================================== */

/* Apply styles only to docs pages, not the homepage */
.docs-wrapper .docMainContainer_node_modules-\@docusaurus-theme-classic-lib-theme-DocPage-Layout-Main-styles-module {
    background-color: transparent; /* Remove default background */
}

.docs-wrapper .docItemCol_node_modules-\@docusaurus-theme-classic-lib-theme-DocItem-Layout-styles-module {
    max-width: 960px; /* Set a max-width for readability */
    margin: 0 auto;
    width: 100%;
}

.docItemContainer_src-theme-DocItem-styles-module {
    padding: 2rem 2.5rem;
    border-radius: 12px;
    background: rgba(255, 255, 255, 0.6); /* Light theme glassmorphism */
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);
    box-shadow: 0 8px 32px 0 rgba(100, 100, 100, 0.1);
    margin-top: 2rem;
}

[data-theme='dark'] .docItemContainer_src-theme-DocItem-styles-module {
    background: rgba(30, 30, 30, 0.6); /* Dark theme glassmorphism */
    border: 1px solid rgba(255, 255, 255, 0.1);
    box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.2);
}

/* ==========================================================================
   Docs Page - Typography and Readability
   ========================================================================== */

.docs-wrapper .markdown {
    line-height: 1.7;
}

.docs-wrapper .markdown p,
.docs-wrapper .markdown ul,
.docs-wrapper .markdown ol {
    font-size: 1.05rem;
    margin-bottom: 1.5rem;
}

.docs-wrapper .markdown h2 {
    font-size: 2.25rem;
    padding-bottom: 0.5rem;
    border-bottom: 1px solid var(--ifm-color-emphasis-300);
    margin-top: 3rem;
    margin-bottom: 1.5rem;
}

.docs-wrapper .markdown h3 {
    font-size: 1.75rem;
    margin-top: 2.5rem;
    margin-bottom: 1rem;
}

/* ==========================================================================
   Sidebar Styling
   ========================================================================== */

.menu__link {
    transition: background-color 0.2s ease, color 0.2s ease;
    border-radius: 6px;
    margin: 2px 0;
}

.menu__link:hover,
.menu__link--active {
    background-color: var(--ifm-color-primary-lightest);
    color: var(--ifm-color-primary-dark);
}

.menu__link--active {
    font-weight: 600;
}

[data-theme='dark'] .menu__link:hover,
[data-theme='dark'] .menu__link--active {
    background-color: rgba(var(--ifm-color-primary-rgb), 0.1);
    color: var(--ifm-color-primary-light);
}

/* ==========================================================================
   Breadcrumbs Styling
   ========================================================================== */

.breadcrumbs {
    background-color: rgba(255, 255, 255, 0.4);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    padding: 0.75rem 1.5rem;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    margin: 1rem 0 0;
    display: inline-block;
}

[data-theme='dark'] .breadcrumbs {
    background-color: rgba(30, 30, 30, 0.4);
    border-color: rgba(255, 255, 255, 0.1);
}

.breadcrumbs__link {
    color: var(--ifm-font-color-secondary);
    transition: color 0.2s ease;
}

.breadcrumbs__link:hover {
    color: var(--ifm-color-primary);
    text-decoration: none;
}

.breadcrumbs__item--active .breadcrumbs__link {
    color: var(--ifm-font-color-base);
    font-weight: 600;
}
```

**`src/theme/DocItem/index.tsx`**
```typescript
import React from 'react';
import DocItem from '@theme-original/DocItem';
import type DocItemType from '@theme/DocItem';
import type {WrapperProps} from '@docusaurus/types';
import styles from './styles.module.css';
import clsx from 'clsx';

type Props = WrapperProps<typeof DocItemType>

export default function DocItemWrapper(props: Props): JSX.Element {
  return (
    <div className={clsx(styles.docItemContainer)}>
        <DocItem {...props} />
    </div>
  );
}
```

**`src/theme/DocItem/styles.module.css`**
```css
.docItemContainer :global(header) {
    text-align: center;
}

.docItemContainer :global(h1) {
    font-size: 3rem;
    font-weight: 800;
    background: linear-gradient(45deg, var(--ifm-color-primary), var(--ifm-color-primary-dark));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 2rem;
}

[data-theme='dark'] .docItemContainer :global(h1) {
    background: linear-gradient(45deg, var(--ifm-color-primary-light), var(--ifm-color-primary-lighter));
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
```
