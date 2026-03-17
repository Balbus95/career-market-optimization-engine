---
description: Gather current labor market data from authoritative sources and output it structured for updating references/market_data.md.
---

# `update-market-data` Workflow

**Trigger:** When the user types `Update Market Data` or `/update-market-data`.

**Action:**
Use your **live web search tools** to gather current labor market data. Do NOT rely on training data for figures that change over time.

### RESEARCH PROTOCOL

**Mandatory sources (minimum baseline):**
- LinkedIn Talent Insights / LinkedIn Jobs trending roles
- Stack Overflow Developer Survey (latest edition)
- Glassdoor / Levels.fyi for compensation data
- World Economic Forum Future of Jobs Report (latest)
- ISTAT / Eurostat for Italian/EU labor market data (if region = Italy/EU)

**Additional sources:** Search any other authoritative sources identified as relevant (e.g., industry-specific reports, company salary databases, government labor statistics). Quality and recency take priority over source loyalty.

### STEPS
1. Search each source for: top in-demand skills, salary benchmarks by role/seniority/region, emerging roles, ATS algorithm updates, LinkedIn best practices.
2. Output the gathered data as a Markdown block **structured identically to `references/market_data.md`**, ready to copy-paste into that file.
3. Flag the date of each data point so the user knows how fresh the information is.

**Output Rules:**
Always cite the source and date for every data point. If a source is inaccessible or outdated, flag it and use the next best alternative.

### 🔗 RECOMMENDED NEXT STEPS
- `/v2c-salary`: To use the fresh salary benchmarks for a new valuation.
- `/job-hunt`: To search for the "emerging roles" identified in the research.
- `/skill-gap`: To see if the "top in-demand skills" create new gaps in your profile.

