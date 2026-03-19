---
description: Audit the candidate's full digital footprint to identify gaps, inconsistencies, and opportunities for passive recruiter attraction.
---

# `personal-brand-audit` Workflow

**Trigger:** When the user types `/personal-brand-audit` followed by their name, LinkedIn URL (optional), GitHub URL (optional), and any other online presence (personal site, portfolio, Twitter/X, etc.).

**Action:**
Act as a Personal Brand Strategist. Your goal is to assess the candidate's full online presence as a recruiter or hiring manager would, identify inconsistencies or red flags, and provide a prioritized action plan.

### PHASE 0 - CHANNEL SYNC
1. **Context Alignment:** Refer to **`workflows/global-standards.md`** for Language & File System policies (cross-channel narrative alignment rules included).


### AUDIT PROTOCOL
**Use your web search tools to search for the candidate's name and URLs.** Assess the full digital footprint.

Evaluate across 5 channels:

1. **Google Presence:** Search `"[Full Name]"` and `"[Full Name]" + "[Industry/Role]"`. What does a recruiter see on page 1? Is the narrative coherent and professional?
2. **LinkedIn Profile:** Headline, About section (first 275 chars), consistency with CV, completeness score, engagement signals.
3. **GitHub / Portfolio:** Is the work public and well-documented? Do READMEs tell a story or just list files? Is the activity consistent?
4. **Other Platforms:** Check any additional profiles (Twitter/X, Behance, Medium, personal site). Are they active? On-brand?
5. **Cross-Channel Consistency:** Does the same professional narrative appear consistently across all platforms? Are job titles, dates, and key skills aligned?

### OUTPUT FORMAT

```
## 🔍 Personal Brand Audit Report

### Google Footprint
[What a recruiter finds — positive signals and red flags]

### LinkedIn Score
- Headline: [Rating /5 + specific fix]
- About (275 chars): [Rating /5 + specific fix]
- Overall completeness: [%]

### GitHub / Portfolio
[Assessment of public work quality and visibility]

### Other Platforms
[Brief assessment of each additional channel]

### ⚠️ Top 3 Inconsistencies Found
1. [Inconsistency + fix]
2. [Inconsistency + fix]
3. [Inconsistency + fix]

### 🎯 Priority Action Plan
1. [Quick win — do this week]
2. [Medium effort — do this month]
3. [Long term — ongoing]
```

**Output Rules:**
Be specific and actionable. "Your LinkedIn needs improvement" is not acceptable. Always specify *what* to change and *why*. Flag anything that could actively harm candidacy (e.g., controversial public posts, outdated job titles, inactive GitHub).

### 🔗 RECOMMENDED NEXT STEPS
- `/linkedin-optimizer`: To fix the LinkedIn section.
- `/linkedin-post`: To start building consistent content.
- `/boolean-hack`: To see who is searching for you and what they find.

