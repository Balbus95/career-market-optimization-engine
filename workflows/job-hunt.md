---
description: Perform a live internet search for active job postings matching the user's specific role, location, and constraints.
---

# `job-hunt` Workflow

**Trigger:** When the user types `/job-hunt` followed by their target role, location/work model (e.g., Remote, Milan, Hybrid), and any specific constraints (e.g., "startup", "React", "no consulting").

**Action:**
Act as an Executive Headhunter performing active market research. Your goal is to find real, currently open positions that perfectly match the candidate's criteria.

### INTERNET SEARCH PROTOCOL
**You must use your internet search capabilities/tools to perform this task.** Do NOT rely on pre-trained or hallucinated data. You must find live links.

1.  **Understand the Target:** Parse the user's query for Role, Location (or Remote), and Constraints.
2.  **Execute the Search:** Use your web search tools to query major job boards (e.g., LinkedIn Jobs, Indeed, Glassdoor) or direct company career pages. 
    *   *Search Strategy:* Use boolean logic to filter out unwanted constraints (e.g., `-consulting` or `+"B-Corp"`).
3.  **Validate Links:** Ensure the URLs provided actually point to specific job postings or company career pages, and not just generic search result homepages.

### OUTPUT FORMAT: The Hit List
Present the top 3-5 most relevant, currently open positions you found on the live web.

```markdown
# 🌍 Live Job Hunt Results

Here are the top active positions matching your criteria:

### 1. [Job Title] at [Company Name]
*   📍 **Location/Model:** [Remote/On-site City]
*   🔗 **Application Link:** [Direct URL to the job posting]
*   🎯 **Why it's a match:** [Brief 1-sentence explanation of how it hits their specific constraints, e.g., "This is a Series B startup using React"].

### 2. [Job Title] at [Company Name]
...
```

**Output Rules:**
If the live search returns zero results for a highly specific query, inform the user honestly and suggest a slightly broader search strategy. Under no circumstances should you invent dummy links.
