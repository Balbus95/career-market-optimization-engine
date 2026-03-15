---
description: Tailor a Master CV to a specific Job Description (JD) to maximize keyword alignment and ATS match rate.
---

# `tailor-cv` Workflow

**Trigger:** When the user types `/tailor-cv` followed by their Master CV (or a link to it) and a Job Description (or a link to it). Read the URL content if a link is provided.

**Action:**
Act as a strict Resume Engineer. Your goal is to perform a "Vertical Extraction" (Phase 1.2 of the Engine) by filtering and rewriting the Master CV to perfectly align with the provided Job Description.

### PHASE 1 - JD DECONSTRUCTION
Analyze the Job Description and extract:
1. **Hard Skills & Tools:** The non-negotiable technical requirements.
2. **Soft Skills:** The cultural and interpersonal traits emphasized.
3. **Exact Match Keywords:** Specific phrases repeated in the JD that ATS systems will look for.

### PHASE 2 - CV FILTERING & REORDERING
* **Remove Fluff:** Discard any bullet points from the Master CV that are completely irrelevant to the JD.
* **Prioritize:** Move the most relevant experiences and skills to the top of their respective sections.

### PHASE 3 - KEYWORD INJECTION & REWRITING
* Seamlessly integrate the extracted exact match keywords into the candidate's existing STAR bullet points.
* Ensure the terminology matches the JD (e.g., if the CV says "Client Management" but the JD asks for "Stakeholder Engagement", update the terminology).
* Maintain the STAR framework and quantifiable metrics.

**Output Rules:**
Output the fully tailored CV in a clean, ATS-friendly markdown format. Do NOT use multi-column layouts or tables. Include a brief summary at the top explaining the major keyword adaptations made.
