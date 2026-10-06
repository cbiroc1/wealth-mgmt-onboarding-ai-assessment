# Requirements Document — User Stories for Top 2 AI Improvements

**Project:** Wealth Management Client Onboarding — AI Opportunity Assessment
**Source of truth:** `analysis/AI_augmentation_analysis.pdf`, `deliverables/time_savings_table.pdf`, and `deliverables/opportunity_matrix.xlsx` (October 2026)
**Prepared for:** Engineering / implementation hand-off
**Author:** Christopher Biroc
## Why Steps 4 and 7

The AI Augmentation Analysis (`analysis/AI_augmentation_analysis.pdf`) scores all seven onboarding steps on two views — the Composite/Tier method (weighted across five rubric dimensions) and the Implementation Complexity vs. AI Value Potential 2×2. The two views give the same designation for three steps (1, 6, and 7) and different designations for four (2, 3, 4, and 5). **Steps 4 and 7 are the two strongest candidates for AI improvement and are the focus of this requirements document.** Step 7 is a Quick Win under both views. Step 4 is a Quick Win in the 2×2, has the highest composite score of any Near-Term step (3.95, just below the 4.00 Quick Win threshold), and carries the highest Process Friction / Failure Exposure score in the matrix (5/5):

| Step | Composite / Tier | 2×2 Quadrant | Risk Level |
| --- | --- | --- | --- |
| 4. Account Setup & Documentation | 3.95 · Near-Term (highest under Composite/Tier) | Quick Win | Low-Medium |
| 7. Welcome & Ongoing Service | 4.30 · Quick Win (highest in the matrix) | Quick Win | Lowest |

Both steps are high-volume, rule-based, and carry no fiduciary or investment-recommendation exposure — unlike Steps 2, 3, 5, and 6, where regulatory judgment (FINRA Rule 2111, SEC Reg BI, fiduciary duty under the Investment Advisers Act of 1940) caps how much of the task can be automated.

---

## User Story 1 — Intelligent Account Document Assembly (Step 4: Account Setup & Documentation)

**As a** financial advisor / operations associate,
**I need** an automated document-assembly system that pre-populates account agreements, disclosure forms, and beneficiary designations from existing CRM data, delivers them via e-signature, and flags NIGO (Not In Good Order) issues before submission to the custodian,
**so that** NIGO-driven rework and correction cycles — the single largest friction point in the onboarding process — are substantially reduced and account opening no longer stalls on manual form preparation.

### Business Justification

- Composite score 3.95 (Near-Term tier, highest score achieved outside Step 7) and Quick Win under the 2×2 view.
- Scores the ceiling of the matrix (5/5) on Process Friction / Failure Exposure — industry NIGO rejection rates run 15–30% of new account paperwork (Cerulli, Docupace, DST Systems), each rejection adding 2–5 days to the onboarding cycle.
- Automation feasibility (4/5) and data availability (4/5) are both strong: most identity and account details already live in the CRM by this stage from discovery and KYC.
- Reference technology: Docupace Digital Account Opening Platform. Documented case studies show 60–80% NIGO reduction from intelligent document-assembly platforms (Docupace, Laser App).
- Estimated impact: ~45–70 minutes of advisor/ops time saved per client; ~20–40 minutes of client time saved (fewer re-signature requests); ~2–5 business days saved in onboarding cycle time — the largest cycle-time driver in the matrix.
- Risk Level: Low-Medium. FINRA Rule 4512 sets account-information standards and Rule 3110 requires supervisory controls, but a NIGO rejection caught pre-submission is an operational exception, not a compliance violation.

### Acceptance Criteria

1. Given a client who has completed discovery and KYC, the system pulls existing CRM data (name, DOB, SSN/EIN, address, account type, beneficiary information) and auto-populates all required account agreements, disclosure forms, and beneficiary designation documents without advisor re-keying.
2. Given a populated document set, the system runs pre-submission validation checks — SSN/EIN format, address match, beneficiary percentages summing to 100%, all required fields and signature blocks present — and blocks submission until validation passes or an exception is acknowledged.
3. Given a validated document package, the system delivers it to the client for e-signature (DocuSign, Adobe Sign, or equivalent) within 2 minutes of the advisor triggering the workflow.
4. Given a document that fails validation, the system routes it to an operations/advisor exception queue with a specific reason code (not just a generic failure) rather than silently blocking submission.
5. Given a completed onboarding cycle, the system logs submission timestamp, validation results, any exceptions raised, and human overrides, to support the FINRA Rule 3110 supervisory-controls audit trail.
6. NIGO rejection rate is tracked monthly at the account level and reported against a target of at least 50% reduction from current baseline; the validation rule set is updated when new custodian reject reasons emerge.
7. All processing occurs within the firm's existing data-governance boundary — no client PII leaves the CRM/document-assembly environment except to the designated e-signature vendor.

---

## User Story 2 — Automated Onboarding Orchestration & Welcome Communication (Step 7: Welcome & Ongoing Service Setup)

**As a** client-service associate / advisor,
**I need** an automated workflow that triggers on account-opening completion to send a personalized welcome communication, finalize the CRM record, schedule the first review meeting, and configure the client's ongoing reporting cadence,
**so that** every client receives a consistent, immediate welcome experience without manual, per-client setup work, freeing advisor and service-staff time for higher-value client interaction.

### Business Justification

- Composite score 4.30 — the highest score in the matrix — and Quick Win under the 2×2 view, the only step to clear the Quick Win threshold under both scoring methods.
- Automation feasibility (5/5) and Time & Volume Benchmarks (5/5) are both at the ceiling: this workflow fires for every client, continuously, making it the highest-frequency step in the process.
- Reference technology: Salesforce Financial Services Cloud + Agentforce (Microsoft Power Automate as an alternative).
- Estimated impact: ~20–25 minutes of advisor/service-staff time saved per client, recurring; ~5–15 minutes of client time saved through immediate welcome/CRM setup; ~1–2 business days saved by removing the queue behind manual follow-up.
- Risk Level: Lowest in the matrix. Only baseline compliance duties apply — Regulation S-P (safeguarding client information) and standard books-and-records requirements — with no per-client fiduciary or investment determination involved.

### Acceptance Criteria

1. Given a completed account-opening event (Step 4 sign-off), the system automatically creates or finalizes the client's CRM record — advisor assignment, account details, and stated goals — without manual data entry.
2. Given a finalized CRM record, the system generates and sends a personalized welcome communication using CRM data (client name, stated goals, assigned advisor) within a defined SLA (target: within minutes of account opening, not hours or days).
3. Given a new client record, the system automatically schedules the first review meeting according to the firm's standard cadence and creates the corresponding calendar/CRM task for the advisor.
4. Given a new client record, the system configures the client's ongoing reporting cadence (statement frequency, performance-report delivery) per firm defaults, with the ability for the advisor to override before the first report cycle.
5. Given any step in the workflow that requires judgment (e.g., a non-standard reporting request or a communication requiring firm-specific disclosure language), the system routes it to advisor/service-staff review rather than sending it automatically — human sign-off is required on any client-facing communication or CRM change that requires judgment.
6. All automated actions (CRM updates, communications sent, meetings scheduled) are logged with timestamp and triggering event to satisfy standard books-and-records requirements under Regulation S-P.
7. Workflow completion — from account-opening event to fully configured client record — is measurable and reported monthly against the target of near-real-time setup (minutes, not days).

---

## Traceability

Both user stories are drawn directly from the AI Augmentation Analysis (`analysis/AI_augmentation_analysis.pdf`), the Time Savings Table (`deliverables/time_savings_table.pdf`), and the Step-by-Step AI Augmentation Opportunities for Steps 4 and 7, and are consistent with the Composite/Tier and 2×2 scoring in the Prioritization Snapshot table of that analysis. No user stories are written for Steps 2, 3, 5, or 6 in this document, as those steps involve a regulated determination (KYC/AML risk rating, suitability, IPS judgment, or investment recommendation) and none of them reaches the Quick Win quadrant of the 2×2.
