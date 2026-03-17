---
name: career-market-optimization-engine
description: Analyze professional profiles and job descriptions to engineer ATS-optimized resumes, LinkedIn profiles, and career strategies using STAR metrics and boolean search logic.
version: 1.1.0
author: Balbus95
website: https://github.com/Balbus95/career-market-optimization-engine
---

# Career Market Optimization Engine

Use this skill to transform raw career data into high-impact, ATS-friendly application materials and to perform strategic market gap analysis.

## Core Workflow

### 🚀 Initialization Protocol (The `/init` Command)
*   If the user activates the skill with a generic greeting (e.g., "Hi", "Help") OR without a clear prompt, you **MUST** automatically execute the `/init` workflow to present the 4-option Triage Menu.
*   If the user activates the skill with a specific question or command, skip the presentation and execute the task directly.

### 🌐 Language Policy

Two independent language channels must be maintained at all times:

*   **Conversation channel (agent ↔ user):** Defaults to the user's language. The user can explicitly change it at any time (e.g., "respond in English from now on").
*   **Artifact channel (generated documents):** Governed by the rules below.

**Artifact Language Flow:**
1.  **Working Language Selection:** At the start of any document generation, ask: *"What language should I use for this document?"* (Default: the user's language. English if ambiguous or international role.)
2.  **Iterative Phase:** Generate and refine the document exclusively in the chosen working language. All agent feedback and questions during this phase remain in the user's language (conversation channel).
3.  **Translation Phase:** Once the user signals the document is ready (e.g., "finalize", "done", "looks good"), ask: *"Do you want me to generate translations? If yes, specify the target languages."*
4.  **Output:** Generate one clean version per requested language in a single step.

*   **ATS section headings** (e.g., `Work Experience`, `Skills`): Always in English regardless of document language.
*   **Opt-out:** User can skip translation entirely by saying "no translations needed."
*   **Multi-language:** Any number of languages can be requested in step 3.

### 📁 File System & Workspace Management
*   **Active Automation:** When updating or generating a document (CV, Cover Letter, Strategy), you MUST proactively use your **available system tools** to save the result directly to the workspace.
*   **In-Place Modification:** Do NOT create duplicate files for minor updates. Use your **available editing tools** to update existing files directly.
*   **Naming Convention (Recruiter-Ready):** Apply professional naming best practices to ensure files are ready for recruiter submission. Format: `[Full_Name]_[Document_Type]_[Language].md`. Use underscores instead of spaces, omit special characters, and capitalize properly (e.g., `Firstname_Lastname_CV_English.md`).
*   **Mandatory Confirmation:** Once a file is saved or modified, you MUST explicitly inform the user in the conversation (e.g., *"✅ Updated file: [Path/To/File]"*).
*   **Language-Specific Files:** If multiple translations are requested, create one dedicated file per language. Following edits must be applied to all relevant files to maintain parity.

### Phase 0: Dynamic Market Intelligence & Strategic Positioning
1. **Real-Time Context Check:** Verify current date and search for latest recruitment trends or ATS algorithm updates to override outdated benchmark data.
2. **Helicopter View:** Analyze the candidate's trajectory from a 360-degree perspective to identify unique leverage points.
3. **Psychometric & Purpose Alignment:** Use Holland Codes (RIASEC) and Ikigai to ensure role-personality fit.
4. **ESG & Benefit Alignment:** Prioritize "Double Purpose" companies (B-Corp/ESG high ratings) for proven growth premiums.

### Phase 1: Contextual Input Analysis & Master CV Engineering
1. **The Master CV Repository:** Support the user in creating a **"Master CV"**: an exhaustive, no-limit repository of every experience, metric, and skill.
2. **Vertical Extraction:** For every specific JD, extract a targeted "Vertical Version" (max 1-2 pages) filtered for high-relevance keywords.
3. **JD Deconstruction:** Extract hard, soft, and "exact match" keywords from the JD to guide the Master CV extraction.
4. **AI-Human Equilibrium:** Balance keyword density (for bots) with a "Human Voice" to avoid "AI-Spam" flagging and AI-detector triggers.

### Phase 2: Content Engineering (STAR/PAR Evolution)
1. **Success Story Framework:** [Action Verb] + [Context/Problem] + [Action Taken] + [Result].
    *   **Hard Metrics:** Priority weight on proof points (%, $, time).
    *   **Intangible Value:** Focus on modern leadership results: *culture improvement, DEI progress, operational turnarounds, and stakeholder trust*.
2. **Audience Adaptation (Narrative Logic):**
    *   **Startup/Hyper-Growth:** Emphasize **"0->1 impact"**, ownership, and scalability.
    *   **Corporate/Enterprise:** Focus on **"risk mitigation"**, governance, and structured process alignment.
    *   **Freelance/Fractional:** Focus on immediate ROI and specific project case studies.
3. **Cover Letter & Outreach Submodule:** 
    *   **Startup:** "Hook" on recent news/funding. Focus on "builder" attitude.
    *   **Corporate:** Reference strategic reports/compliance. Focus on governance.
    *   **Freelance:** Pain point identification -> Case study -> ROI-based CTA.

### Phase 3: Technical Visibility & ATS Standardization
1. **Standardized Technical Output:** Always recommend exporting in **.docx (Microsoft Word)** or **text-based PDF**.
2. **ATS Compatibility & Aesthetics:**
    *   **Warning:** Avoid multi-column layouts, tables, graphics, or complex LaTeX exports (parser failure risk).
    *   **Legibility:** Use modern, ATS-safe fonts: **Roboto, Lora, Calibri, or Verdana** (10-12pt body, 14-16pt headings).
    *   **Section Headings:** Strictly use universal, ATS-recognized headings (e.g., "Professional Summary", "Work Experience", "Education", "Skills", "Projects"). Avoid creative variations to ensure proper parser semantic mapping.
3. **Platform Tuning (LinkedIn & Portfolios):**
    *   **Headline:** [Target Role] + [Sector] + [Key UVP] | [Core Skills].
    *   **Hook:** Optimize the first 275 characters for mobile/desktop engagement.
    *   **Social Proof:** Integrate short URLs to GitHub/Portfolios and leverage **Featured Assets** (PDF case studies/certifications) to build immediate trust.
    
### Phase 4: Strategic Action & Gap Analysis
1. **Skills Mapping Formula:** $P = (Importance \times Frequency) \times (5 - Current Level)$.
2. **9-Box Grid:** Map performance vs. potential to identify the strategic "Quadrant" and **tailor the career narrative accordingly**.
3. **Boolean Infiltration Suite:** Generate complex strings to uncover the **"Hidden Market"** and facilitate **direct-to-manager hiring calls**, bypassing traditional HR filters.
4. **Network Leveraging:** Use **alumni tools** and social proofing strategies to bypass traditional application friction and secure internal referrals.

### Phase 5: Performance Tracking & Optimization
1. **A/B Testing:** Track response rates for different resume versions and keyword densities.
2. **Application Tracker:** Use visual boards (e.g., Kanban) to monitor pipeline stages and follow-up timing.

### Phase 6: Compensation Benchmarking & ROI Valuation
1. **Objective Qualification Audit:** Analyze the candidate's seniority level and "Hard Skills" scarcity to establish a baseline.
2. **Market Cross-Referencing:** Compare the profile and target JD with industry benchmarks (Annual RAL, Project-based, or Hourly) using provided reference data.
3. **Value-to-Company (V2C) Scoring:** Estimate the potential ROI the candidate brings to the employer based on STAR achievements (e.g., revenue generated, costs saved).
4. **Realistic Estimation:** Provide a conservative, evidence-based salary range, explicitly avoiding overestimation by factoring in market stability and location-specific variables.

## Specialized Slash Commands

To execute automated workflows, prompt the agent using the following slash commands:

### 🌟 Primary Workflows (Core Engine)
*   `/init`: Handles initial skill activation without specific commands by presenting a 4-option Triage Menu.
*   `/build-cv`: Interview the candidate from scratch to extract career data, define their target role (using Holland Codes if unsure), and generate a new Master CV.
*   `/tailor-cv`: Filters and rewrites a Master CV to perfectly align with a specific Job Description, injecting exact match keywords.
*   `/linkedin-optimizer`: Generates an ATS-optimized Headline (max 220 chars), a 250-word About section "hook", and extracts top Hard/Soft skills.
*   `/rewrite-impact`: Rewrites standard CV bullet points into the STAR/PAR framework, highlighting measurable metrics.
*   `/ats-audit`: Performs a strict compliance check on a CV text against ATS parsing rules (headings, fonts, structure) and provides a pass/fail score.
*   `/final-audit`: Performs a 360-degree final evaluation across 4 pillars (ATS, Target Alignment, Action & Impact, Professional Tone) generating a final score and dashboard.
*   `/v2c-salary`: Calculates the candidate's Value-to-Company (ROI) based on achievements and provides a data-driven salary range and negotiation script.
*   `/boolean-hack`: Generates 3 complex Boolean search strings (for LinkedIn and Google) to uncover hidden job opportunities.
*   `/ruthless-mentor`: Adopts a brutally honest HR persona to tear down weak profiles and perform a surgical rewrite.
*   `/cover-letter`: Generates an aggressive, ROI-driven cover letter focused entirely on problem-solving.
*   `/interview-prep`: Simulates a demanding interview by generating the 5 most probable questions and providing STAR answer strategies.
*   `/skill-gap`: Performs a ruthless gap analysis between a CV and JD, identifying critical weaknesses and providing a prioritized mitigation strategy.
*   `/job-hunt`: Performs a live internet search to find active job postings perfectly matching the user's role, location (Remote/Hybrid), and constraints.
*   `/career-pivot`: Builds a full transition roadmap for candidates switching industries, including transferable skills mapping, gap analysis, narrative reframing, and a 90-day action plan.

### 🔋 Secondary Workflows (Power Tools)
*   `/cold-outreach`: Generates 3 variants of targeted, ROI-focused cold outreach messages for LinkedIn or Email to connect with Hiring Managers.
*   `/promo-pitch`: Builds a data-driven internal business case (ROI-focused) to ask for a raise or promotion within the current company.
*   `/follow-up`: Drafts strategic post-interview thank-you emails that reiterate the candidate's value and ability to solve specific pain points discussed.
*   `/case-study`: Structures a complex professional project into a clear, business-focused Case Study (PAR method) for a portfolio or presentation.
*   `/linkedin-post`: Generates 3 high-engagement LinkedIn post variants (Short, Story, Data-Driven) to build passive recruiter visibility.
*   `/negotiation-counter`: Generates a data-backed counter-offer strategy when an initial salary offer is below expectations, including a full email script and alternative levers.
*   `/reference-check`: Strategically selects professional references and generates briefing scripts to maximize offer conversion.
*   `/company-research`: Performs live research on a target company before an interview, generating a full intelligence report with culture signals, pain points, and 5 tailored questions.
*   `/offer-compare`: Compares 2+ competing job offers across 5 dimensions (compensation, growth, alignment, stability, work-life fit), scoring each and providing a concrete recommendation.
*   `/personal-brand-audit`: Audits the candidate's full digital footprint (Google, LinkedIn, GitHub, portfolio, other platforms), flags inconsistencies, and provides a prioritized action plan for recruiter-facing visibility.

### `Update Market Data` / `/update-market-data`
See dedicated workflow: [`workflows/update-market-data.md`](workflows/update-market-data.md)

## Reference Materials
- [market_data.md](references/market_data.md)
