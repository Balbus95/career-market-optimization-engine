# 🚀 Career Market Optimization Engine

> **An advanced, data-driven engine for ATS optimization, salary benchmarking, and career growth strategy.**

The Career Market Optimization Engine transforms raw career data into high-impact, ATS-friendly application materials. Designed for professionals who want to optimize their career trajectory, it acts as a strategic career consultant using evidence-based market data and proven methodologies (like the STAR/PAR framework and Holland Codes).

---

## 🌟 Core Capabilities & Value Proposition

### 1. ATS Structural Conformance Engineering
*   **The Challenge:** Formatting errors cause silent rejection before any human review — ~75% of resumes are filtered out by parsers before a recruiter sees them.
*   **The Engine's Solution:** Enforces **structural conformance** with the parsing grammar of major ATS engines (Workday, Greenhouse, Lever, iCIMS), then extracts targeted 1-2 page vertical versions aligned to the JD. The hiring decision moves back onto the content — where it belongs. (This reduces format-based rejection risk; it does not guarantee selection.)

### 2. Evidence-Based Compensation Benchmarking
*   **The Challenge:** Uncertainty during salary negotiations or lack of data justifying higher compensation.
*   **The Engine's Solution:** Utilizes reference market data and "Value-to-Company" (V2C) logic to provide realistic, ROI-focused salary estimations. It formulates justifications tied directly to your quantifiable achievements and hard metrics.

### 3. Mobile-First LinkedIn Visibility (275-Character Engineering) & Advanced Prospect Research
*   **The Challenge:** Recruiters see a truncated mobile preview before deciding to click — and most hidden roles are never posted on aggregator boards.
*   **The Engine's Solution:** Engineers the exact first 275 characters of your LinkedIn About section as a recruiter-facing hook (LinkedIn's mobile "...see more" cutoff), with character-count validation. Combined with **Advanced Prospect Research** (Boolean strings built on the same Direct-to-Manager methodology Sales SDRs use for B2B prospecting), this creates a two-sided visibility loop: inbound (recruiters find you) + outbound (you find Hiring Managers directly).

### 4. Strategic Content Re-engineering (STAR)
*   **The Challenge:** Generic experience descriptions that fail to demonstrate real impact.
*   **The Engine's Solution:** Rewrites professional achievements using the precise STAR methodology (Action Verb + Context/Problem + Action Taken + Result/Metric). This ensures a professional, ROI-focused, and data-driven narrative adaptable to Startup, Corporate, or Freelance environments.

---

## 🛠️ Operational Workflow

The engine operates through strictly structured phases to enforce methodological consistency:

*   **Phase 0:** Dynamic Market Intelligence & Strategic Positioning
*   **Phase 1:** Contextual Input Analysis & Master CV Engineering
*   **Phase 2:** Content Engineering (STAR/PAR Evolution)
*   **Phase 3:** Technical Visibility & ATS Standardization
*   **Phase 4:** Strategic Action & Gap Analysis
*   **Phase 5:** Performance Tracking & Optimization
*   **Phase 6:** Compensation Benchmarking & ROI Valuation

---

## ⚠️ System & Context Limitations

Given the complexity of the analytical workflows, the Engine operates best with high-tier LLM models capable of handling large context windows. 

*   **Heavy Workflows:** Commands like `/job-hunt` (live web scraping), `/build-cv` (iterative data extraction), and `/final-audit` (360-degree evaluation) require significant processing power and memory.
*   **Free Tier Warning:** Users on free AI tiers may experience context truncation, memory limits, or degraded performance during these heavy tasks. For the optimal experience across all phases, using a premium LLM subscription is highly recommended.

---

## 📖 The Operating Manual: How to Use the Engine

Instead of generic prompts, the Engine is equipped with automated **Slash Commands**. You can think of them as specialized agents ready to process your documents.

### Unsure where to start?
Just write "Hi", "Help", or **`/init`** to activate the engine. It will automatically present you with a **6-option Triage Menu** to route you to the correct tool depending on your current needs.

### Phase 0: Dynamic Market Intelligence & Strategic Positioning
*   **`/career-context`**: Your first move. Builds or updates your strategic dossier (`career_dossier.md`) — a persistent SSOT file containing your positioning, hidden skills, target company preferences, and post-graduation checklist. All other commands load this file automatically to skip redundant questions.
*   **`/build-cv`**: Start from scratch. The engine will interview you, help you find your target role if unsure, and build a 100% ATS-compliant Master CV.

### Phase 1: Contextual Input Analysis & Master CV Engineering
*   **`/tailor-cv`**: 
    *   *What it does:* You provide your Master CV and a Job Description. It extracts a perfectly tailored 1-page "Vertical CV", filtering out irrelevant fluff and injecting the exact-match keywords the ATS is looking for.
*   **`/skill-gap`**:
    *   *What it does:* Cross-references your CV with a Job Description. It highlights your critical weaknesses, partial matches, and provides a prioritized strategy on how to mitigate them (e.g., what to study, how to pivot).

### Phase 2: Content Engineering (STAR/PAR Evolution)
*   **`/rewrite-impact`**:
    *   *What it does:* Takes your boring "task-based" bullet points (e.g., *"Responsible for managing the team"*) and re-engineers them into the STAR framework (e.g., *"Spearheaded a team of 5, reducing delivery time by 20%..."*). It will explicitly ask you for missing metrics.
*   **`/linkedin-optimizer`**:
    *   *What it does:* Takes your CV and generates an SEO-optimized LinkedIn Headline (max 220 chars); engineers the first 275 characters of the About section for mobile-feed visibility (the "...see more" cutoff); writes the full About section (200-250 words); and lists 15 Hard Skills & Tools + 5 Soft Skills to pin to your profile.
*   **`/ruthless-mentor`**:
    *   *What it does:* Acts as a brutally honest Fortune 500 HR director. It performs an "autopsy" on your Professional Profile, destroys your cliches, cross-examines your vague claims, and rewrites it surgically.

### Phase 3: Technical Visibility & ATS Standardization
*   **`/final-audit`**:
    *   *What it does:* The Ultimate Gatekeeper. It performs a 360° check on your final CV across 4 pillars (ATS Parseability, Target Alignment, Action-Orientation & Impact, and Tone & Professionalism), generating a visual dashboard with a final score (0-100) and your top 3 mandatory fixes.
*   **`/ats-audit`**:
    *   *What it does:* Acts as an ATS parser. It scans your final CV text to ensure you used standard headings (e.g., "Work Experience", not "My Journey") and warns you of formatting that could break the parsing software.
*   **`/cover-letter`**:
    *   *What it does:* Generates a highly aggressive, ROI-driven cover letter focused entirely on problem-solving. No generic cliches.

### Phase 4: Strategic Action & Gap Analysis
*   **`/job-hunt`**:
    *   *What it does:* The Live Radar. Feed it a role, location (Remote/Hybrid/City), and constraints, and it browses the live web to find 5-10 curated opportunities returning direct links.
*   **`/boolean-hack`**:
    *   *What it does:* **Advanced Prospect Research via Boolean strings.** Applies the same Direct-to-Manager prospecting methodology used by Sales SDRs — rewritten for candidates. Builds targeted Boolean queries (Google X-Ray, LinkedIn Sales Navigator syntax) to surface Hiring Managers, Talent Acquisition leads, and live job posts published outside aggregator boards.
*   **`/interview-prep`**:
    *   *What it does:* Simulates a demanding interview. Based on your CV and the JD, it predicts the 5 most difficult/probable questions and helps you map your STAR achievements to the answers.
*   **`/v2c-salary`**:
    *   *What it does:* The Value-to-Company calculator. It uses the **`scripts/calculate_v2c.py`** tool to estimate a realistic salary range based on market data and the ROI of your achievements, providing a negotiation script and evidence-backed anchors.
*   **`/career-pivot`**:
    *   *What it does:* Builds a full transition roadmap for career changers: maps transferable skills, identifies gaps, rewrites your narrative for the new industry, and generates a 90-day action plan.

### 🔋 Secondary Workflows (Power Tools)
These tools handle the crucial peripheral steps of career advancement:
*   **`/cold-outreach`**: Generates 3 variants of aggressive, ROI-focused cold messages to send to Hiring Managers on LinkedIn or via Email.
*   **`/follow-up`**: Drafts strategic post-interview thank-you emails that reiterate exactly how you will solve the pain points discussed in the interview.
*   **`/case-study`**: Takes a messy brain-dump of a project you completed and structures it into a sleek, business-focused "Problem-Action-Result" Case Study for your portfolio.
*   **`/promo-pitch`**: Builds a data-driven internal business case (ROI-focused) to present to your boss when asking for a raise or promotion.
*   **`/linkedin-post`**: Generates 3 viral-optimized LinkedIn post variants (Short, Story, Data-Driven) to build passive recruiter visibility.
*   **`/negotiation-counter`**: Generates a precise counter-offer strategy with a full email script and non-salary levers when an offer is below expectations.
*   **`/reference-check`**: Strategically selects your references and generates briefing scripts to ensure they reinforce the right narrative.
*   **`/company-research`**: Deep-dives on a target company before an interview — culture, financials, recent news, pain points, and 5 tailored questions to ask.
*   **`/offer-compare`**: Compares 2+ competing offers across compensation, growth, stability, and role-fit, scoring each and giving a direct recommendation.
*   **`/personal-brand-audit`**: Scans your full digital footprint (Google, LinkedIn, GitHub, portfolio), flags inconsistencies across platforms, and gives a prioritized action plan to maximize passive recruiter attraction.

### 🔄 Maintenance
*   **`/update-market-data`**: Queries live authoritative sources (LinkedIn Talent Insights, Stack Overflow Survey, Glassdoor, WEF Future of Jobs) and outputs a structured Markdown block ready to replace `references/market_data.md`. Run periodically to keep salary benchmarks and skill demand data current.

*(You can still prompt the engine naturally for custom requests, e.g., "Analyze this Job Description and give me general advice...").*

---
## 📂 Repository Contents

*   **Strategic Workflows (`SKILL.md`):** Comprehensive system constraints, operational flows, and narrative logic.
*   **Automated Commands (`workflows/`):** Slash commands (`/career-context`, `/linkedin-optimizer`, `/ats-audit`, etc.) to execute specific tasks instantly.
*   **Strategic Dossier (`career_dossier.md`):** Auto-generated SSOT file created by `/career-context`. Loaded automatically by all workflows to avoid redundant questions and provide persistent candidate context.
*   **System Context (`GEMINI.md`):** Core mandates and tone guidelines for AI processing.
*   **Market Data (`references/market_data.md`):** Evidence-based salary and skill demand benchmarks.
*   **Calculators (`scripts/`):** Python tools for objective analysis:
    *   `calculate_priority.py`: For skill gap prioritization.
    *   `calculate_v2c.py`: For ROI-based salary benchmarking.
*   **Global Standards (`workflows/global-standards.md`):** The centralized source of truth for all workflows (STAR+, V2C, ATS, and Channel Sync).
*   **Output Template (`assets/cv_template.html`):** ATS-safe HTML shell for zero-dependency PDF generation. Open in any browser and use `Ctrl+P → Save as PDF`.

---

## 📥 Installation

Install the extension directly via `npx` (recommended):

```bash
npx skills add https://github.com/Balbus95/career-market-optimization-engine --skill career-market-optimization-engine
```

*Alternatively, you can use the Gemini CLI:*
```bash
gemini extensions install https://github.com/Balbus95/career-market-optimization-engine
```

---

## 📜 License
Free to use and share under the MIT License.
