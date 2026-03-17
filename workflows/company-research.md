---
description: Deep-dive research on a target company before an interview, generating strategic context and tailored questions.
---

# `company-research` Workflow

**Trigger:** When the user types `/company-research` followed by the target company name and role applied for.

**Action:**
Act as an Intelligence Analyst preparing a candidate for a high-stakes interview. Use your web search capabilities to gather real, live data on the company.

### PHASE 0 - CHANNEL SYNC
1. **Language Check:** Reports are usually generated in the user's conversation language for quick internal review.
2. **File Automation:** Propose to save the intelligence report to the workspace (e.g., `[Company]_Research.md`).

### RESEARCH PROTOCOL
**You must use your internet search tools to find current, accurate information.** Do NOT rely on training data for facts that change over time (revenue, headcount, news).

Search for and synthesize:
1. **Company DNA:** Mission, business model, main products/services, key markets.
2. **Financial Health:** Recent funding rounds, revenue figures, profitability signals, or stock performance (if public).
3. **Culture Signals:** Glassdoor/Blind reviews sentiment, known values, remote/hybrid policy.
4. **Recent News:** Last 90 days — acquisitions, layoffs, launches, pivots, or leadership changes.
5. **Pain Points:** Identify likely challenges the company is currently facing based on news/market trends. These are your interview gold.
6. **The Team:** Find the LinkedIn of the interviewer or hiring manager (if inferable). Note their background and tenure.

### OUTPUT FORMAT

```
## 🏢 Company Intelligence Report: [Company]

### Business Snapshot
[3-4 sentences: what they do, who their customers are, competitive position]

### Financial Health
[Key signals — stage, funding, revenue if public, growth trajectory]

### Culture & Work Environment
[Sentiment summary from reviews + known policies]

### Recent News (Last 90 Days)
- [Headline] — [Brief implication for the candidate]

### Likely Pain Points
- [Pain point] — [How your skills could address it in the interview]

### 5 Smart Questions to Ask the Interviewer
1. [Specific, researched question]
```

**Output Rules:**
Only include verified, sourced facts. Flag any uncertain data with *(unverified)*. If search returns no results for a field, say so honestly.

### 🔗 RECOMMENDED NEXT STEPS
- `/interview-prep`: To use the "Likely Pain Points" and "Smart Questions" in a mock session.
- `/tailor-cv`: To align your CV with the company's DNA discovered here.
- `/v2c-salary`: To estimate your worth based on the company's financial health.

