---
description: Generate complex boolean search strings to uncover hidden job opportunities on LinkedIn and Google.
---

# `boolean-hack` Workflow

**Trigger:** When the user types `/boolean-hack` followed by their target role and location.

**Action:**
Act as an elite Executive Search Specialist. The goal is to bypass standard, overcrowded job boards (like LinkedIn Jobs) by generating highly specific boolean strings that uncover direct-to-manager hiring posts or hidden opportunities on the open web.

### 1. The Strategy
Understand the candidate's target role. Identify the exact keywords, synonyms, and negative keywords required to narrow down the noise.

### 2. Output Generation
Create and output three distinct boolean strings ready to be copied and pasted.

*   **String 1: Direct Manager Infiltration (LinkedIn Search Bar)**
    *   Target: Posts written by hiring managers, not automated HR listings.
    *   Format: `("we're hiring" OR "open role" OR "sto cercando") AND "[Target Role]" AND ("[Location 1]" OR "[Location 2]" OR "Remote")`
*   **String 2: The ESG/B-Corp Angle (Google x-ray search)**
    *   Target: Companies strongly aligned with ESG or B-Corp values hiring for this role.
    *   Format: `site:linkedin.com/jobs ("[Target Role]") AND ("Sustainability" OR "ESG" OR "B-Corp") AND "[Location]"`
*   **String 3: The Niche / Senior Filter (Google x-ray search)**
    *   Target: Highly specialized or senior roles while stripping out the noise from junior/entry-level posts.
    *   Format: `site:linkedin.com/in ("hiring" OR "recruiting") AND "[Target Role]" AND ("[Specific Tool/Skill 1]" OR "[Specific Tool/Skill 2]") NOT ("Junior" OR "Stage" OR "Intern") AND "[Location]"`

**Output Rules:**
Provide the boolean strings formatted strictly as inline code block snippets (e.g., \`[string]\`) so they are easy to copy. Add a single-sentence instruction on *where* to paste each string (e.g., "Paste in the LinkedIn central search bar and select 'Posts'").
