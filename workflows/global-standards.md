# Career Market Engine: Global Standards

These standards govern ALL content generation and analysis within the engine. Referencing this file ensures consistency across all 26+ workflows.

## 1. The Success Story Framework (STAR+)
Every professional bullet point MUST follow this logic:
- **Action Verb:** Strong, non-generic (e.g., "Engineered" instead of "Worked on").
- **Context/Problem:** The specific challenge or scale (e.g., "during a 30% budget cut").
- **Action Taken:** The unique intervention performed.
- **Metric/Result:** Hard proof (%, $, ⏱️) or documented Qualitative Impact.

## 2. Value-to-Company (V2C) Formula
When estimating salary or impact, use the logic from `scripts/calculate_v2c.py`:
$$V2C = (Generated Revenue + Cost Savings) \times [(Complexity \times 0.5) + (Scarcity \times 0.5)]$$

## 3. Skill Priority Formula
When performing gap analysis, use the logic from `scripts/calculate_priority.py`:
$$P = (Importance \times Frequency) \times (5 - Current Level)$$

## 4. Technical Document Standards
- **Primary Engine Format:** Single-column Markdown.
- **Output Tiers:**
    *   **Tier 1 (Universal):** HTML Shell (No dependencies).
    *   **Tier 2 (Pro):** LaTeX/Pandoc/Local Scripts.
- **Headings:** Default to ATS-standard headings (Professional Summary, Work Experience, Education, Skills, Projects). User-defined headings are allowed **only on explicit user request**; the AI must flag the ATS compatibility risk in-conversation.
- **Fonts (Recommended):** Roboto, Arial, Calibri, Verdana (modern web-safe stack).
- **Tone:** Technical, ROI-driven, data-backed. No flowery language.

## 5. Channel Sync Policy
At the start of ANY document generation:
1. Confirm **Working Language**.
2. Perform **In-Place Modification** of existing workspace files if present.
3. Apply **Bilingual Output** (Italian/English default) unless opted out.
4. **Confirm** save path to the user.
