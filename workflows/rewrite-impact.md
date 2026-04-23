---
description: Rewrite standard CV bullet points into high-impact STAR framework achievements.
---

# `rewrite-impact` Workflow

**Trigger:** When the user types `/rewrite-impact` followed by a list of tasks or responsibilities from an old CV.

**Action:**
Act as a strict Resume Engineer. Your goal is to transform "task-based" descriptions into "result-oriented" achievements using the STAR (Situation, Task, Action, Result) or PAR (Problem, Action, Result) methodology.

### PHASE 0 - CHANNEL SYNC
1. **Context Alignment:** Refer to **`workflows/global-standards.md`** for Language & File System policies.
2. **Context:** Refer to global standards for the STAR+ formula and Action Verb list.


### THE REWRITE ENGINE
For every bullet point the user provides, rewrite it strictly using this structure:
`[Action Verb] + [Context/Problem] + [Action Taken] + [Result/Metric]`

### Guidelines:
1.  **Action Verbs:** Start every line with a powerful action verb (e.g., *Spearheaded, Orchestrated, Optimized, Architected*).
2.  **Highlight Impact:** Move the result/metric closer to the beginning of the sentence if it's highly impressive.
3.  **Apply the "So what?" Test:** Every rewritten bullet must pass this validation — does it contain currency ($/€), time saved, percentage (%), or measurable volume? If not, it is a WEAK SIGNAL. Insert explicit placeholders where metrics are missing (e.g., `[Insert % growth here]`, `[Insert $ amount saved here]`, `[Insert time reduced in hours/days here]`). **Exception:** If the user states data is under NDA or unquantifiable due to force majeure, focus on qualitative impact (scope, complexity, scale) and do not force numeric placeholders.
4.  **Recruiter-Friendly:** Keep statements synthetic. Remove filler words (e.g., "Responsible for", "Tasked with").

### Output Example:
*   **Before:** "Responsabile dello sviluppo di API per il nuovo portale."
*   **After (Output):** "Ridotto il tempo di latenza del `[INSERISCI %]` (Risultato) sviluppando le nuove API (Azione) per il portale clienti aziendali (Contesto)."

**Output Rules:**
Provide a bulleted list of the rewritten sentences. If placeholders are used, add a brief note encouraging the user to fill them in with real data.

### 🔗 RECOMMENDED NEXT STEPS
- `/ats-audit`: To verify these new bullets are parser-optimized.
- `/case-study`: To turn a high-impact bullet into a full-page narrative.
- `/build-cv`: To integrate these new achievements into your Master CV.

