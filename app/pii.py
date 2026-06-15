from __future__ import annotations

import hashlib
import re

PII_PATTERNS: dict[str, str] = {
    "email": r"[\w\.-]+@[\w\.-]+\.\w+",
    "phone_vn": r"(?:\+84|0)[ \.-]?\d{3}[ \.-]?\d{3}[ \.-]?\d{3,4}", # Matches 090 123 4567, 090.123.4567, etc.
    "cccd": r"\b\d{12}\b",
    "credit_card": r"\b\d{4}[- ]?\d{4}[- ]?\d{4}[- ]?\d{4}\b",
    # TODO: Add more patterns (e.g., Passport, Vietnamese address keywords)
    "passport": r"(?i)\b[a-z]\d{7}\b",
    "address_vn": r"(?i)\b(?:số\s+\d+\s+)?(?:đường|phố|quận|huyện|phường|tỉnh|thành\s+phố|xã|street|district|ward|province|city)\b",

}


def log_audit(event: str, **payload) -> None:
    import json
    from datetime import datetime, timezone
    audit_record = {
        "ts": datetime.now(timezone.utc).isoformat() + "Z",
        "event": event,
        "payload": payload
    }
    try:
        with open("data/audit.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(audit_record) + "\n")
    except Exception:
        pass


def scrub_text(text: str) -> str:
    safe = text
    for name, pattern in PII_PATTERNS.items():
        if re.search(pattern, safe):
            log_audit("pii_redacted", type=name, preview=safe[:30] + "...")
        safe = re.sub(pattern, f"[REDACTED_{name.upper()}]", safe)
    return safe


def summarize_text(text: str, max_len: int = 80) -> str:
    safe = scrub_text(text).strip().replace("\n", " ")
    return safe[:max_len] + ("..." if len(safe) > max_len else "")


def hash_user_id(user_id: str) -> str:
    return hashlib.sha256(user_id.encode("utf-8")).hexdigest()[:12]
