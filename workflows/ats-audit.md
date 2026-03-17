---
description: Perform a strict ATS-compliance audit on a provided CV text.
---

# `ats-audit` Workflow

**Trigger:** When the user types `/ats-audit` and provides their full CV text.

**Action:**
### PHASE 0 - CHANNEL SYNC
1. **Context Alignment:** Refer to **`workflows/global-standards.md`** for Language & File System policies.
2. **Workspace Scan:** Check for existing CV/Audit files to perform in-place updates.


### Audit Checklist:

1.  **Section Headings:** Verify that *only* standard, universal ATS headings are used (e.g., "Professional Summary", "Work Experience", "Education", "Skills", "Projects"). Flag creative variations like "What I do", "My Journey", or "Core Competencies" as errors.
2.  **Structural Issues:** Check for cues of complex formatting (tables, columns, graphics). While you are analyzing text, advise the user that the final export *must* be a clean, single-column `.docx` or text-based PDF without styling tricks.
3.  **Keyword Density:** Skim the text to see if there is a healthy balance of Hard Skills vs. Soft Skills.
4.  **Action Verbs:** Check if the experience bullet points start with strong action verbs and contain quantifiable metrics.

### Output Format:
Provide the results in a clear "Traffic Light" format:
*   🔴 **CRITICAL ERRORS:** Formatting or naming conventions that will cause an immediate parsing failure.
*   🟡 **WARNINGS:** Areas that are parsed but lack impact (e.g., missing metrics, weak verbs).
*   ✅ **PASS:** Elements that are perfectly structured.

**Final Score:** Give a final "ATS Compatibility Score" out of 100. If the score is below 90, clearly state that the CV should not be submitted until the errors are fixed.
