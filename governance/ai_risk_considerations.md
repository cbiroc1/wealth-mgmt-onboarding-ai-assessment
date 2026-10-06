# AI Risk Considerations
### Wealth Management Client Onboarding - AI Opportunity Assessment

This document looks at the main risks and governance considerations for the two AI opportunities selected for the initial phase of the wealth management onboarding project. The focus is on where AI can improve the process without taking over decisions that should remain with an advisor or operations team.

## Scope

The two opportunities selected for initial deployment are:

1. **Step 7 - Welcome & Ongoing Service Setup** (Composite Score: 4.30, Quick Win)
2. **Step 4 - Account Setup & Documentation** (Composite Score: 3.95, Near-Term Priority)

Step 7 received the highest score in the opportunity matrix because the work is highly repeatable, happens for every client, and involves relatively little regulatory judgment. Step 4 is a little more complex, but it has a strong opportunity to reduce rework and delays during account opening.

The other five onboarding steps are not included in the initial deployment. They either scored lower in the matrix or require a level of advisor judgment that makes them less appropriate for early automation.

## Governance Framework

The risk assessment uses two main references.

- **NIST AI Risk Management Framework (AI RMF 1.0)** provides the overall structure for thinking about AI risk through Govern, Map, Measure, and Manage.
- **FINRA's 2026 Annual Regulatory Oversight Report, GenAI section** is used as the securities-industry reference point. It highlights issues such as accuracy, hallucinations, data quality, bias, supervision, testing, monitoring, governance, and human review.

The important point is that using AI does not remove the firm's existing regulatory responsibilities. The technology changes how work is performed, but it does not change who is responsible for the outcome.

## Step 7 - Welcome & Ongoing Service Setup

**Composite Score: 4.30 | Tier: Quick Win | Tool: Salesforce Financial Services Cloud + Agentforce**

This is the clearest starting point for AI augmentation. The activities being considered here are routine tasks such as creating CRM records, sending standard welcome communications, and setting up recurring service workflows.

The opportunity matrix scored this step:

- **Automation Feasibility: 5/5**
- **Time & Volume Benchmarks: 5/5**
- **Risk (inverse): 5/5**

The main reason this step has a lower risk profile is that it occurs after the major client and investment decisions have already been made. It is not being used to determine suitability or make an investment recommendation.

### Main Risks

**Client data exposure.** CRM automation and client communications involve personal and account information. A poorly configured workflow or overly broad data field could send information to the wrong system or include information that should not have been part of the communication.

**Accuracy of client-facing content.** Even a simple welcome email can create a problem if the AI inserts the wrong account information, makes a statement that is not accurate, or communicates something outside the firm's approved language. This is where FINRA's concerns around accuracy and hallucinations become relevant.

**Records retention.** Automated communications still need to be retained appropriately. Because these workflows could run automatically for every client, the recordkeeping process needs to be part of the design rather than something added later.

**Expanding the use case too far.** The fact that this step is easy to automate does not mean every ongoing client communication should be automated. Routine communications are different from communications that require judgment about a client's circumstances.

### Controls

Client-service staff should review exceptions and any communication or CRM change that requires judgment before it is finalized. The initial implementation should stay limited to the specific routine workflows included in the assessment.

I would also use periodic sampling of AI-generated communications to check accuracy and confirm that the CRM and communication systems are retaining the appropriate records.

## Step 4 - Account Setup & Documentation

**Composite Score: 3.95 | Tier: Near-Term | Tool: Docupace Digital Account Opening Platform**

Step 4 has a different risk profile. There is a strong efficiency case because account documentation is repetitive and much of the required information already exists in the CRM or was collected during earlier onboarding steps. At the same time, errors at this stage can directly affect whether an account is opened successfully.

The opportunity matrix scored this step:

- **Automation Feasibility: 4/5**
- **Data Availability: 4/5**
- **Process Friction / Failure Exposure: 5/5**
- **Risk (inverse): 4/5**

Industry estimates cited in the project materials put NIGO (Not In Good Order) rejection rates around 15–30% for new-account paperwork, with problems potentially adding several days to the onboarding process.

### Main Risks

**Poor upstream data.** AI can only work with the information it receives. If information from Discovery or KYC is incorrect, incomplete, or inconsistent, an automated document process can carry that problem forward instead of fixing it.

**Missed errors.** An automated validation step should reduce NIGO problems, but it could also create a false sense of security if it misses an issue that a human reviewer would have caught.

**Supervisory responsibility.** Automating form population does not remove the firm's responsibility to supervise the account-opening process. There should be evidence that the appropriate person reviewed the documents before submission.

**Sensitive documents.** Account opening can involve identity documents, proof of address, and other financial information. Vendor security, data retention, and how information moves between systems need to be reviewed before implementation.

### Controls

Operations or advisor staff should review exceptions and validate completed account documentation before the account is submitted.

A useful way to measure whether the implementation actually works would be to compare NIGO rates before and after deployment. The project materials reference vendor case studies showing potential NIGO reductions of roughly 60–80%, but those numbers should be treated as a benchmark to test rather than an expected result.

I would also audit a sample of accounts that the system clears without an exception. Looking only at flagged accounts could miss the more important problem: an error the system failed to identify.

## Governance Requirements Across Both Steps

A few controls apply to both opportunities.

**Keep a human in the process.** Human review is part of the design of these use cases. It is not simply a backup plan if the AI fails. The scoring assumes that people remain responsible for exceptions and decisions that require judgment.

**Review the vendor before deployment.** Both use cases involve client information. Security controls, data storage, retention, access, and data residency should be reviewed before production use.

**Monitor after implementation.** A successful pilot does not mean the risk is solved. Step 7 should be monitored through periodic reviews of generated communications. Step 4 should be measured through NIGO rates, exception rates, and audits of accounts cleared by the system.

**Keep the scope narrow.** The scores in the opportunity matrix are based on specific use cases. If the firm later wants to use AI for more complex client communications, suitability decisions, investment recommendations, or other activities, that should be evaluated separately rather than assuming the original approval covers the new use.

## Sources

- Regulation S-P
- FINRA Rule 4512 - Customer Account Information
- FINRA Rule 3110 - Supervision
- FINRA 2026 Annual Regulatory Oversight Report - GenAI section
- NIST AI Risk Management Framework (AI RMF 1.0)
- Cerulli Associates
- Docupace and DST Systems NIGO / document-assembly case studies
- Laser App
- Journal of Computer Science and Technology Studies - data readiness research
- World Economic Forum / Capgemini - data readiness research
- IBM Institute for Business Value - AI-ready data
- Salesforce Financial Services Cloud and Microsoft Power Automate product documentation

*Research sources supporting the scoring are listed in `data/scoring_data_sources.md`. Composite scores and tiers come from `analysis/AI_augmentation_analysis.pdf` and `deliverables/opportunity_matrix.xlsx`.*
