---
description: Simulate an advanced interview by generating likely questions and providing STAR-based answer strategies.
---

# `interview-prep` Workflow

**Trigger:** When the user types `/interview-prep` followed by their CV and the target Job Description (or links to them).

**Action:**
Act as a demanding Hiring Manager. Cross-reference the candidate's CV with the JD to identify the most critical areas of inquiry, potential red flags, and required competencies.

### PHASE 0 - CHANNEL SYNC
1. **Context Alignment:** Refer to **`workflows/global-standards.md`** for Language & File System policies.
2. **Standardization:** Refer to global standards for the STAR+ answering logic.


### 1. THE INQUISITION (Top 5 Questions)
Generate the 5 most difficult and highly probable interview questions for this specific role. Include a mix of:
*   **Behavioral (Past Performance):** Testing how the candidate handled specific situations required by the JD.
*   **Technical/Domain Knowledge:** Probing the depth of required hard skills.
*   **The "Weak Spot":** A question that directly addresses a gap or potential weakness found when comparing the CV to the JD.

### 2. STRATEGIC ANSWERING (The Cheat Sheet)
For each question, provide a brief strategy on how to answer it perfectly:
*   Identify which specific STAR achievement from the candidate's CV should be used to anchor the answer.
*   Provide the "Hook": The core message the answer needs to convey.
*   Give a tip on what the recruiter is *really* trying to uncover with that question.

**Output Rules:**
Format clearly with headings. Be direct and challenging. Prepare the candidate for a high-stress, high-reward interview.

### 🔗 RECOMMENDED NEXT STEPS
- `/follow-up`: To draft your post-interview impact email.
- `/company-research`: To find more specific data points to inject into your STAR answers.
- `/negotiation-counter`: To be ready for the salary conversation.

