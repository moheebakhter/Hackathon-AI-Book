---
id: 103
title: "Enlarge Docusaurus Navbar Logo"
stage: green
date_iso: "2025-12-10"
surface: "agent"
model: "gemini-1.5-pro"
feature: "none"
branch: "main"
user: "unknown"
command: "unknown"
labels: ["docusaurus", "frontend", "css", "navbar"]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files_yaml:
 - "docusaurus.config.ts"
 - "src/css/custom.css"
tests_yaml:
 - "none"
---

# Enlarge Docusaurus Navbar Logo

## PROMPT

You are an expert Docusaurus customization engineer.

Your task is to modify ONLY the navbar logo size.  
Do NOT modify anything else.  
Do NOT touch homepage UI, docs UI, components, or layout.

========================
🎯 GOAL
========================
Make the navbar logo significantly larger and more visible.

========================
📂 FILES TO MODIFY
========================

1) docusaurus.config.ts  
   - Update navbar.logo to include a bigger width and height

2) src/css/custom.css  
   - Add CSS override to ensure the logo displays at the desired size  

========================
🛠 REQUIRED OUTPUT FORMAT
========================

OUTPUT SECTION 1:  
Updated logo config for docusaurus.config.ts  
(size increased using width, height or style properties)

OUTPUT SECTION 2:  
CSS override for src/css/custom.css  
(to force the navbar logo to render larger, e.g., 40–50px height)

========================
⚠ RULES
========================
- Do NOT modify any other file  
- Do NOT modify homepage  
- Do NOT modify sidebar  
- Do NOT modify docs  
- Only change navbar logo size  
- No explanations  
- Output clean replace-ready code  

========================
Now generate the updated code to enlarge the logo.

## RESPONSE

**`docusaurus.config.ts`**
```typescript
      logo: {
        alt: 'Physical AI Logo',
        src: 'img/logo.png',
        width: 160,
        height: 48,
      },
```

**`src/css/custom.css`**
```css
/* ==========================================================================
   Navbar Logo Customization
   ========================================================================== */
:global(.navbar__brand img) {
    height: 48px !important; /* Force a larger height */
    max-height: 48px !important;
    width: auto !important;
}

/**
 * Any CSS placed here will be applied to the whole site,
 * affecting both the homepage and docs pages.
 *
 * For styles specific to docs pages, use selectors that
 * target elements within the documentation layout.
 */
```
