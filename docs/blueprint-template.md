# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: NguyenThanhLoc
- [REPO_URL]: https://github.com/looby239/2A202600817-NguyenThanhLoc-Day13
- [MEMBERS]:
  - Member A: NGUYEN_THANH_LOC | Role: Logging & PII
  - Member B: NGUYEN_THANH_LOC | Role: Tracing & Enrichment
  - Member C: NGUYEN_THANH_LOC | Role: SLO & Alerts
  - Member D: NGUYEN_THANH_LOC | Role: Load Test & Dashboard
  - Member E: NGUYEN_THANH_LOC | Role: Demo & Report

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: 10
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: docs/assets/Langfuse-trace-list.PNG
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: docs/assets/Log-line-with-PII-redaction.PNG
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: docs/assets/Full-trace-waterfall.PNG
- [TRACE_WATERFALL_EXPLANATION]: Trace waterfall shows parent span `run` calling sub-spans `retrieve` and `generate`. During the rag_slow incident, `retrieve` span takes 2500ms while `generate` takes only 150ms.

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: docs/assets/Dashboard.PNG
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | 2758ms |
| Error Rate | < 2% | 28d | 0% |
| Cost Budget | < $2.5/day | 1d | $0.02 |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: docs/assets/alert_rules.PNG
- [SAMPLE_RUNBOOK_LINK]: [docs/alerts.md#L1]

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Độ trễ phản hồi trung bình (P95) của API tăng vọt lên khoảng 2.7 giây cho các câu hỏi cần tìm kiếm dữ liệu RAG, gây ảnh hưởng xấu tới trải nghiệm người dùng và suýt vi phạm SLO độ trễ.
- [ROOT_CAUSE_PROVED_BY]: Trace ID 60863fcbd9b7398b5744cb0bd07eff30
- [FIX_ACTION]: Tắt mô phỏng sự cố: `python scripts/inject_incident.py --scenario rag_slow --disable`. Về lâu dài, cấu hình timeout (ví dụ: 1.0s) cho RAG tool.
- [PREVENTIVE_MEASURE]: Thiết lập cảnh báo tự động khi độ trễ P95 > 3000ms kéo dài liên tục, cấu hình caching cho các truy vấn phổ biến và xây dựng cơ chế fallback khi RAG bị chậm.

---

## 5. Individual Contributions & Evidence

### [NGUYEN_THANH_LOC] 2202600817 
- [TASKS_COMPLETED]: Hoàn thành toàn bộ bài Lab bao gồm: Thiết lập Correlation ID middleware, làm giàu log (enrichment), mở rộng regex lọc dữ liệu PII nhạy cảm, cấu hình bộ lọc PII cho structlog, tích hợp tracing qua Langfuse v3, cấu hình Alert rules và Runbooks, chạy kịch bản sự cố và load test, xây dựng Dashboard và cài đặt các tính năng điểm thưởng (Cost Optimization, Audit Logs, Custom Quality Metrics).
- [EVIDENCE_LINK]: https://github.com/looby239/2A202600817-NguyenThanhLoc-Day13/commits/main

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: Đã triển khai cơ chế Dynamic Routing định tuyến các truy vấn ngắn (<50 ký tự) hoặc tác vụ tóm tắt (`summary`) sang mô hình giá rẻ `claude-haiku-3-5` (giúp giảm chi phí tới 91.7%). Thông tin model tương ứng được tag trực tiếp lên Langfuse.
- [BONUS_AUDIT_LOGS]: Đã xây dựng cơ chế ghi nhật ký kiểm toán (Audit Logs) độc lập lưu vào `data/audit.jsonl`. Ghi lại toàn bộ các sự kiện nhạy cảm như bật/tắt incident (`incident_enabled`/`incident_disabled`) và các sự kiện lọc thông tin cá nhân PII (`pii_redacted`).
- [BONUS_CUSTOM_METRIC]: Đã tích hợp độ đo chất lượng phản hồi tự động `quality_score` vào in-memory metrics (`app/metrics.py`) và hiển thị điểm chất lượng trung bình qua `/metrics`.
