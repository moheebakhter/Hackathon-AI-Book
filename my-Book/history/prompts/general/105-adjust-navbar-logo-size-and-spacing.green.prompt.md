---
id: 105
title: "Adjust Navbar Logo Size and Spacing"
stage: green
date_iso: "2025-12-10"
surface: "agent"
model: "gemini-1.5-pro"
feature: "none"
branch: "main"
user: "unknown"
command: "unknown"
labels: ["docusaurus", "frontend", "css", "navbar", "logo", "spacing"]
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

# Adjust Navbar Logo Size and Spacing

## PROMPT

You are an expert Docusaurus customization engineer.

Your task is to modify ONLY the navbar appearance by increasing the logo size and adjusting its alignment and spacing on the left side.

Do NOT modify homepage, docs pages, theme layout, or any other part of the site.

========================
🎯 GOAL
========================
1️⃣ Increase the navbar logo size significantly (height 50–65px)  
2️⃣ Add proper spacing between logo and site title (“Docs”)  
3️⃣ Ensure the entire left navbar section is visually balanced and not stuck to the edge  
4️⃣ Apply CSS overrides if Docusaurus default sizing limits the logo  

========================
📂 FILES TO MODIFY
========================
1) docusaurus.config.ts  
   - Update navbar.logo (width/height/style)

2) src/css/custom.css  
   - Add CSS override for larger logo  
   - Add spacing between logo + title  
   - Add padding-left for left navbar container  

========================
🛠 REQUIRED OUTPUT FORMAT
========================

OUTPUT SECTION 1:  
Updated navbar.logo config for docusaurus.config.ts  
(size and spacing)

OUTPUT SECTION 2:  
CSS override for src/css/custom.css  
(to enforce larger logo size + left spacing + logo-title spacing)

========================
⚠ RULES
========================
- Do NOT modify homepage or hero section  
- Do NOT modify docs layout  
- Do NOT modify feature code  
- Only change navbar logo size + spacing  
- Output clean replace-ready code only  
- No explanations  

========================
Now generate the updated logo size and navbar spacing code.

## RESPONSE

**`docusaurus.config.ts`**
```typescript
      logo: {
        alt: 'Physical AI Logo',
        src: 'img/logoss.png',
        width: 200,
        height: 60,
      },
```

**`src/css/custom.css`**
```css
/* ==========================================================================
   Navbar Customization
   ========================================================================== */
.navbar {
  padding-left: 1.5rem; /* Ensure left section is not stuck to the edge */
}

:global(.navbar__brand img) {
    height: 60px !important; /* Force a larger height */
    max-height: 60px !important;
    width: auto !important;
    margin-right: 1rem; /* Spacing between logo and next item */
}

/* Adjust spacing for the site title next to the logo */
.navbar__title {
  margin-left: 0.5rem;
  font-size: 1.2rem;
  font-weight: 600;
}
```
