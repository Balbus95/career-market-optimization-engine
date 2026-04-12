---
description: Create or update a SSOT file (career_dossier.md) with the candidate's full strategic career context. Preserves existing valid sections on update.
---

# `career-context` Workflow

**Trigger:** When the user types `/career-context`.

**Action:**
Act as a Strategic Career Architect. Your job is to build or update the candidate's Single Source of Truth (SSOT): a persistent `career_dossier.md` file in the working directory. This file becomes the canonical reference for all future skill commands.

---

### PHASE 0 — FILE DETECTION

1. **Check if `career_dossier.md` exists** in the working directory.
   - **If NO → CREATE mode:** Proceed to Phase 1. Collect all data from scratch via structured interview.
   - **If YES → UPDATE mode:** Read the existing file. Identify which sections are already populated. Skip those sections in the interview (do NOT overwrite them unless the user explicitly says "update [section name]"). Only collect data for missing or outdated sections.

2. **Announce the mode** to the user:
   - CREATE: *"No SSOT file found. I'll interview you to build `career_dossier.md` from scratch."*
   - UPDATE: *"Existing SSOT file found. I'll only ask about missing or outdated sections."*

---

### PHASE 1 — DATA COLLECTION (Structured Interview)

Ask the following questions grouped by section. In UPDATE mode, skip questions for sections already populated. Never ask all questions at once — group them by section and wait for the user's reply before moving on.

#### Section A — Strategic Positioning
- What is your current job title (or the title you're targeting)?
- What is your preferred work modality? (Remote / Hybrid / On-site / Flexible)
- What is your employment status? (Employed / Open to offers / Actively job hunting / Freelance)
- What was the score on your last `/final-audit` or `/ats-audit`? (If unknown, write N/A)
- What is your primary target role and sector right now?

#### Section B — Extended Knowledge Base
- List competencies, tools, or methodologies you use regularly but that are NOT currently on your public CV (e.g., internal tools, domain knowledge, soft skills).
- Describe your cloud/infrastructure exposure in detail: which platforms (AWS/GCP/Azure/other), which services, at what level (user / admin / architect)?
- What are your current Work In Progress (WIP) projects? Include personal, academic, or side projects.

#### Section C — Target Company Guidelines
- For each company type below, what is your preference or fit level (Strong / Neutral / Avoid)?
  - Startup / Hyper-Growth
  - Corporate / Enterprise
  - Consulting / Agency
  - Freelance / Fractional
  - Public Sector / NGO
- Are there specific industries, company sizes, or cultures you want to exclude?

#### Section D — Post-Graduation & Recent Activity
- What is your graduation date (or expected date)?
- What academic or extracurricular activities have you done recently that are relevant to your career (theses, certifications, volunteering, competitions, publications)?
- What are the next 3-5 career actions you plan to complete? (These become the checklist.)

---

### PHASE 2 — FILE GENERATION / UPDATE

#### CREATE mode:
Generate the full `career_dossier.md` file using the template below, populated with the collected data.

#### UPDATE mode:
Read the existing file and apply surgical in-place edits:
- Add data to empty sections.
- Append new checklist items without removing completed ones.
- Update the `Last Updated` timestamp.
- Do NOT touch sections the user did not explicitly ask to revise.

Use your available file system tools to write/edit the file directly. Once done, confirm:
*"✅ SSOT updated: `career_dossier.md`"*

---

### FILE TEMPLATE

```markdown
# Career Optimization Master Report
> Single Source of Truth (SSOT) — Career Market Optimization Engine
> Last Updated: {{DATE}}

---

## 1. Strategic Positioning

| Field | Value |
|---|---|
| **Current / Target Title** | {{title}} |
| **Work Modality** | {{modality}} |
| **Employment Status** | {{status}} |
| **Primary Target Role** | {{target_role}} |
| **Target Sector** | {{target_sector}} |
| **Last Audit Score** | {{audit_score}} |

---

## 2. Extended Knowledge Base

### 2.1 Competencies Not on Public CV
{{hidden_skills}}

### 2.2 Cloud & Infrastructure Detail
| Platform | Services Used | Level |
|---|---|---|
{{cloud_table}}

### 2.3 Work In Progress (WIP) Projects
{{wip_projects}}

---

## 3. Target Company Guidelines

| Company Type | Fit | Notes |
|---|---|---|
| Startup / Hyper-Growth | {{fit_startup}} | {{notes_startup}} |
| Corporate / Enterprise | {{fit_corp}} | {{notes_corp}} |
| Consulting / Agency | {{fit_consulting}} | {{notes_consulting}} |
| Freelance / Fractional | {{fit_freelance}} | {{notes_freelance}} |
| Public Sector / NGO | {{fit_public}} | {{notes_public}} |

### Exclusions
{{exclusions}}

---

## 4. Post-Graduation & Recent Activity

**Graduation Date:** {{graduation_date}}

### Recent Activities
{{recent_activities}}

### Future Checklist
- [ ] {{checklist_item_1}}
- [ ] {{checklist_item_2}}
- [ ] {{checklist_item_3}}
```

---

### OUTPUT RULES
- Never generate a markdown code block in the saved file — write plain Markdown directly.
- Always update `Last Updated` to the current date on every write.
- The file must be human-readable and usable as standalone context in any future skill command.
- In UPDATE mode: append checklist items, never delete existing ones (even if completed — the user manages their own checklist).

### 🔗 RECOMMENDED NEXT STEPS
- `/final-audit`: Run a fresh audit with the updated context in mind.
- `/tailor-cv`: Use the extended knowledge base to strengthen a vertical CV version.
- `/boolean-hack`: Use the target role and sector to generate hidden-market search strings.
