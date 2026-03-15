---
description: Analyze a JD against a CV to identify critical skill gaps and prioritize learning.
---

# `skill-gap` Workflow

**Trigger:** When the user types `/skill-gap` followed by their CV and the target Job Description (or links to them).

**Action:**
Act as a Strategic Career Analyst. Perform a ruthless gap analysis to show the candidate exactly where they fall short of the JD requirements and how to mitigate those shortcomings.

### 1. THE AUDIT
Extract all explicit and implicit requirements from the JD (Hard Skills, Soft Skills, Certifications, Years of Experience, specific domain knowledge).
Compare this list against the provided CV.

### 2. THE GAP REPORT
Categorize the findings into:
*   ✅ **Matches:** Requirements the candidate clearly meets (with proof from the CV).
*   🟡 **Partial Matches / Weaknesses:** Areas where the candidate has adjacent experience but lacks the exact keyword or depth required.
*   🔴 **Critical Gaps:** Non-negotiable requirements completely missing from the CV.

### 3. MITIGATION STRATEGY & PRIORITY
For each Partial Match and Critical Gap, calculate a hypothetical priority leveraging the Priority Formula logic ($P = Importance \times Frequency \times Gap$).
Provide a concrete action plan:
*   **Short-Term Fix:** Can this gap be bridged by reframing existing experience or taking a weekend crash course?
*   **Long-Term Goal:** Does this require a formal certification or months of study?
*   **Interview Strategy:** How to handle questions about this gap during the interview (e.g., pivot to a parallel skill, demonstrate fast learning capacity).

**Output Rules:**
Be objective and data-driven. Do not sugarcoat critical gaps.
