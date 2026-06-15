# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: Group E2
- [REPO_URL]: https://github.com/looby239/GroupE2-Day13.git
- [MEMBERS]:
  - Member A: Quyen | Role: Logging & PII
  - Member B: [Name] | Role: Tracing & Enrichment
  - Member C: [Name] | Role: SLO & Alerts
  - Member D: [Name] | Role: Load Test & Dashboard
  - Member E: [Name] | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 10
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: Shown in logs.jsonl and console logs output
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: Verified by validation script output
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: Verified by validation script output
- [TRACE_WATERFALL_EXPLANATION]: The middleware span starts and ends the correlation ID tracking, wrapping the api endpoint execution. Nested inside are the agent.run, mock_rag.retrieve, and FakeLLM.generate child spans, capturing precise execution times and input/output tokens.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: [Pending implementation by Member D]
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 320ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.05 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: [Pending implementation by Member C]
- [SAMPLE_RUNBOOK_LINK]: [docs/alerts.md#L1]

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Requests targeting the "qa" feature had higher latencies (exceeding 300ms) compared to others.
- [ROOT_CAUSE_PROVED_BY]: `latency_ms` and `cost_usd` logged in `data/logs.jsonl` where RAG operations took the bulk of the response time.
- [FIX_ACTION]: [Pending implementation by Member D]
- [PREVENTIVE_MEASURE]: [Pending implementation by Member D]

---

## 5. Individual Contributions & Evidence

### Quyen
- [TASKS_COMPLETED]: 
  - Implemented Correlation ID Middleware in `app/middleware.py`.
  - Enriched structured log context variables with user/session details in `app/main.py`.
  - Added Passport, IP, and Vietnamese Address pattern matching to `app/pii.py`.
  - Registered PII scrubbing processor `scrub_event` in `app/logging_config.py`.
  - Validated logging pipeline and achieved 100/100 score on `validate_logs.py`.
- [EVIDENCE_LINK]: Local commits in repository history.

### [MEMBER_B_NAME]
- [TASKS_COMPLETED]: [Pending]
- [EVIDENCE_LINK]: [Pending]

### [MEMBER_C_NAME]
- [TASKS_COMPLETED]: [Pending]
- [EVIDENCE_LINK]: [Pending]

### [MEMBER_D_NAME]
- [TASKS_COMPLETED]: [Pending]
- [EVIDENCE_LINK]: [Pending]

### [MEMBER_E_NAME]
- [TASKS_COMPLETED]: [Pending]
- [EVIDENCE_LINK]: [Pending]

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: (Description + Evidence)
- [BONUS_AUDIT_LOGS]: (Description + Evidence)
- [BONUS_CUSTOM_METRIC]: (Description + Evidence)
