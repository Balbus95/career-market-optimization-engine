# 🚀 Career Market Optimization Engine

> **An advanced, data-driven engine for ATS optimization, salary benchmarking, and career growth strategy.**

The Career Market Optimization Engine transforms raw career data into high-impact, ATS-friendly application materials. Designed for professionals who want to optimize their career trajectory, it acts as a strategic career consultant using evidence-based market data and proven methodologies (like the STAR/PAR framework and Holland Codes).

---

## 🌟 Core Capabilities & Value Proposition

### 1. ATS-Standardized Master CV Engineering
*   **The Challenge:** High rejection rates due to non-compliant CV formats or lack of keyword optimization.
*   **The Engine's Solution:** Creates a minimalist, structurally optimized "Master CV" and extracts highly targeted 1-2 page vertical versions. It balances Job Description (JD) keyword density with human readability to seamlessly bypass Applicant Tracking Systems (ATS).

### 2. Evidence-Based Compensation Benchmarking
*   **The Challenge:** Uncertainty during salary negotiations or lack of data justifying higher compensation.
*   **The Engine's Solution:** Utilizes reference market data and "Value-to-Company" (V2C) logic to provide realistic, ROI-focused salary estimations. It formulates justifications tied directly to your quantifiable achievements and hard metrics.

### 3. "Hidden Market" Infiltration & Visibility
*   **The Challenge:** Relying solely on public job boards with extremely high competition.
*   **The Engine's Solution:** Generates complex Boolean search strings to uncover hidden job opportunities, facilitating direct-to-manager outreach. It uniquely optimizes the critical first 275 characters of your LinkedIn profile for maximum desktop and mobile engagement.

### 4. Strategic Content Re-engineering (STAR)
*   **The Challenge:** Generic experience descriptions that fail to demonstrate real impact.
*   **The Engine's Solution:** Rewrites professional achievements using the precise STAR methodology (Action Verb + Context/Problem + Action Taken + Result/Metric). This ensures a professional, ROI-focused, and data-driven narrative adaptable to Startup, Corporate, or Freelance environments.

---

## 🛠️ Operational Workflow

The engine operates through strictly structured phases to guarantee strategic alignment:

*   **Phase 0:** Dynamic Market Intelligence & Strategic Positioning
*   **Phase 1:** Contextual Input Analysis & Master CV Engineering
*   **Phase 2:** Content Engineering (STAR/PAR Evolution)
*   **Phase 3:** Technical Visibility & ATS Standardization
*   **Phase 4:** Strategic Action & Gap Analysis
*   **Phase 5:** Performance Tracking & Optimization
*   **Phase 6:** Compensation Benchmarking & ROI Valuation

---

## 📖 The Operating Manual: How to Use the Engine

Instead of generic prompts, the Engine is equipped with 10 automated **Slash Commands**. You can think of them as specialized agents ready to process your documents.

### Phase 0: Creation & Structuring
*   **`/build-cv`**: Start from scratch. The engine will interview you, help you find your target role if unsure, and build a 100% ATS-compliant Master CV.

### Phase 1: Preparation & Alignment
*   **`/tailor-cv`**: 
    *   *What it does:* You provide your Master CV and a Job Description. It extracts a perfectly tailored 1-page "Vertical CV", filtering out irrelevant fluff and injecting the exact-match keywords the ATS is looking for.
*   **`/skill-gap`**:
    *   *What it does:* Cross-references your CV with a Job Description. It highlights your critical weaknesses, partial matches, and provides a prioritized strategy on how to mitigate them (e.g., what to study, how to pivot).

### Phase 2: Content Optimization (STAR Framework)
*   **`/rewrite-impact`**:
    *   *What it does:* Takes your boring "task-based" bullet points (e.g., *"Responsible for managing the team"*) and re-engineers them into the STAR framework (e.g., *"Spearheaded a team of 5, reducing delivery time by 20%..."*). It will explicitly ask you for missing metrics.
*   **`/linkedin-optimizer`**:
    *   *What it does:* Takes your CV and generates an SEO-optimized LinkedIn Headline (max 220 chars), a magnetic "About" section hook (first 275 chars), and lists the top 15 Hard Skills to pin to your profile.
*   **`/ruthless-mentor`**:
    *   *What it does:* Acts as a brutally honest Fortune 500 HR director. It performs an "autopsy" on your Professional Profile, destroys your cliches, cross-examines your vague claims, and rewrites it surgically.

### Phase 3: Validation & Direct Action
*   **`/ats-audit`**:
    *   *What it does:* Acts as an ATS parser. It scans your final CV text to ensure you used standard headings (e.g., "Work Experience", not "My Journey") and warns you of formatting that could break the parsing software.
*   **`/cover-letter`**:
    *   *What it does:* Generates a highly aggressive, ROI-driven cover letter focused entirely on problem-solving. No generic cliches.
*   **`/boolean-hack`**:
    *   *What it does:* You provide a role and a city. It generates 3 advanced Boolean search strings (for Google and LinkedIn) to bypass standard job boards and find hidden posts published directly by Hiring Managers.

### Phase 4: The Interview & Negotiation
*   **`/interview-prep`**:
    *   *What it does:* Simulates a demanding interview. Based on your CV and the JD, it predicts the 5 most difficult/probable questions they will ask you, and tells you *which* of your past achievements to use to answer them perfectly.
*   **`/v2c-salary`**:
    *   *What it does:* The Value-to-Company calculator. It estimates a realistic salary range based on market data and the ROI of your achievements. It provides you with a 3-line negotiation script to justify your request mathematically.

*(You can still prompt the engine naturally for custom requests, e.g., "Analyze this Job Description and give me general advice...").*

---
## 📂 Repository Contents

*   **Strategic Workflows (`SKILL.md`):** Comprehensive system constraints, operational flows, and narrative logic.
*   **Automated Commands (`workflows/`):** Slash commands (`/linkedin-optimizer`, `/ats-audit`, etc.) to execute specific tasks instantly.
*   **System Context (`GEMINI.md`):** Core mandates and tone guidelines for AI processing.
*   **Market Data (`references/market_data.md`):** Evidence-based salary and skill demand benchmarks.
*   **Calculators (`scripts/`):** Python tools (e.g., `calculate_priority.py`) for objective skill gap analysis.

---

## 📥 Installation

Install the extension directly via the Gemini CLI using the following command:

```bash
gemini extensions install https://github.com/Balbus95/career-market-optimization-engine
```

*(Alternatively, you can add it via npx: `npx skills add Balbus95/career-market-optimization-engine`)*

---

## 📜 License
Free to use and share under the MIT License.
