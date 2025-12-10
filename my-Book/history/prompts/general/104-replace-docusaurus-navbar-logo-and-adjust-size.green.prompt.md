---
id: 104
title: "Replace Docusaurus Navbar Logo and Adjust Size"
stage: green
date_iso: "2025-12-10"
surface: "agent"
model: "gemini-1.5-pro"
feature: "none"
branch: "main"
user: "unknown"
command: "unknown"
labels: ["docusaurus", "frontend", "css", "navbar", "logo"]
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

# Replace Docusaurus Navbar Logo and Adjust Size

## PROMPT

You are a Docusaurus customization expert.

Your task is to modify ONLY the navbar logo by replacing it with a new logo file named `logoss.png`, located in the `/static/img/` directory, and make the logo display in a larger size (45–60px height).

Do NOT modify anything else in the project.

========================
🎯 GOAL
========================
1️⃣ Replace the current navbar logo with: /static/img/logoss.png  
2️⃣ Make the new logo appear large and clearly visible (45–60px height)  
3️⃣ Apply CSS overrides if required  
4️⃣ Do NOT change homepage, docs, sidebar, or layout — ONLY navbar logo

========================
📂 FILES TO MODIFY
========================
1) docusaurus.config.ts  
   - Update the navbar.logo configuration  
   - Point to logoss.png  
   - Add width/height or style attribute

2) src/css/custom.css  
   - Add CSS override: large logo size  
   - Ensure the logo displays correctly across light/dark themes

========================
🛠 REQUIRED OUTPUT FORMAT
========================

OUTPUT SECTION 1:  
Updated navbar.logo code for docusaurus.config.ts

OUTPUT SECTION 2:  
CSS override for src/css/custom.css to enforce a larger logo size  

========================
⚠ RULES
========================
- Do NOT modify any other file  
- Do NOT change homepage code  
- Do NOT change docs layout  
- Do NOT rewrite the navbar except logo  
- Only change the logo image + its size  
- Produce clean, replace-ready code only  
- NO explanations  

========================
Now generate the final updated code.

## RESPONSE

**`docusaurus.config.ts`**
```typescript
      logo: {
        alt: 'Physical AI Logo',
        src: 'img/logoss.png',
        width: 160,
        height: 50,
      },
```

**`src/css/custom.css`**
```css
:global(.navbar__brand img) {
    height: 50px !important; /* Force a larger height */
    max-height: 50px !important;
    width: auto !important;
}
```
