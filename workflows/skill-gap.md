---
description: Analyze a JD against a CV to identify critical skill gaps and prioritize learning.
---

# `skill-gap` Workflow

**Trigger:** When the user types `/skill-gap` followed by their CV and the target Job Description (or links to them).

**Action:**
Act as a Strategic Career Analyst. Perform a ruthless gap analysis to show the candidate exactly where they fall short of the JD requirements and how to mitigate those shortcomings.

### PHASE 0 - CHANNEL SYNC
1. **Context Alignment:** Refer to **`workflows/global-standards.md`** for Language & File System policies.
2. **Priority Script:** **You MUST use `scripts/calculate_priority.py`** for gap scoring.


### 1. THE AUDIT
Extract all explicit and implicit requirements from the JD (Hard Skills, Soft Skills, Certifications, Years of Experience, specific domain knowledge).
Compare this list against the provided CV.

### 2. THE GAP REPORT
Categorize the findings into:
*   ✅ **Matches:** Requirements the candidate clearly meets (with proof from the CV).
*   🟡 **Partial Matches / Weaknesses:** Areas where the candidate has adjacent experience but lacks the exact keyword or depth required.
*   🔴 **Critical Gaps:** Non-negotiable requirements completely missing from the CV.

### 3. MITIGATION STRATEGY & PRIORITY
For each Partial Match and Critical Gap, **you MUST execute `scripts/calculate_priority.py`** to get the Priority Score (P).
Provide a concrete action plan based on the script's output:
*   **Status: CRITICAL GAP:** Immediate upskilling required.
*   **Status: HIGH PRIORITY:** Focus for next quarter.
*   **Interview Strategy:** How to handle questions about this gap during the interview (e.g., pivot to a parallel skill, demonstrate fast learning capacity).

**Output Rules:**
Be objective and data-driven. Do not sugarcoat critical gaps.
