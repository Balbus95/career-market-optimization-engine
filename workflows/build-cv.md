---
description: Build a Master CV from scratch through a guided, interactive interview process.
---

# `build-cv` Workflow

**Trigger:** When the user types `/build-cv` (with or without initial notes/links).

**Action:**
### STEP 0 - CHANNEL SYNC & LANGUAGE
1. **Context Alignment:** Refer to **`workflows/global-standards.md`** for Language & File System policies.
2. **Workspace Scan:** Check if a CV file (e.g., `CV_ENG.md`) already exists. Propose to update it directly.

### PHASE 0 - THE COMPASS (Target & Positioning)

1. Ask the user for their target role or industry.
2. **If the user is unsure or lacks a clear target:** Stop and help them find it.
    * Use Phase 0.3 ("Holland Codes/Ikigai") from `SKILL.md`. Ask them what tasks they enjoy most, what problems they are good at solving, and what kind of environment they prefer.
    * **ROI & Salary Maximization:** When suggesting 2-3 potential roles based on their answers, you MUST cross-reference their transferable skills with high-paying market trends (referencing `market_data.md`). Prioritize and propose roles that offer the highest Value-to-Company (V2C) and salary potential, explaining *why* these roles are lucrative.
3. Ask for essential contact data (Name, City/Country, LinkedIn/GitHub links). No photos or physical addresses.

### PHASE 1 - CAREER CHRONOLOGY (Iterative Extraction)
Guide the user through their work history, **one role at a time**, starting with the most recent.
1. Ask for: Company Name, Job Title, Start Date (Month/Year), End Date.
2. Ask them to list 3-4 main tasks or achievements in plain language.
3. **The STAR Enforcement:** Before moving to the next role, aggressively push the user to quantify those tasks.
    * Apply the Rule: `[Action Verb] + [Context/Problem] + [Action Taken] + [Result/Metric]`.
    * Ask probing questions: "How large was the budget?", "By what percentage did efficiency increase?", "How many users were impacted?".
    * *Grace Clause:* If the user invokes NDA or force majeure, pivot to qualitative impact (complexity, cross-functional collaboration, stakeholder level).

### PHASE 2 - EDUCATION & SKILLS
Once all work experience is documented, ask two final questions:
1. Highest relevant Education (Degree, Institution, Dates) and key Certifications.
2. A brain-dump of Hard Skills (Software, Frameworks, Methodologies) and up to 3 Soft Skills.

### PHASE 3 - ASSEMBLY & SUMMARY
1. Draft a powerful 3-line "Professional Summary" based on the extracted data, using an engaging hook (referencing `linkedin-optimizer` logic).
2. Assemble the final Master CV using strict ATS-compliant Markdown.
    * **Heading Hierarchy:** The candidate's full name is the only `#` (H1). All section headings use `##` (H2): `## Professional Summary`, `## Work Experience`, `## Education`, `## Skills`.
    * Ensure a clean, single-column layout with bullet points.

**Output Rules:**
Do not simply list keywords. Integrate them naturally into the bullet points and summary. **Save the final CV directly to the workspace** following the File System naming convention in `SKILL.md` (e.g., `Firstname_Lastname_CV_English.md`). Confirm the file path to the user after saving.

### 🔗 RECOMMENDED NEXT STEPS
- `/cover-letter`: To generate a matching introductory letter.
- `/interview-prep`: To prepare for questions specific to this JD.
- `/ats-audit`: To ensure the tailored version is still parser-friendly.
