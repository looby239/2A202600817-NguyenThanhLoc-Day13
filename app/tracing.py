from __future__ import annotations

import os
from typing import Any
from dotenv import load_dotenv
load_dotenv()

try:
    from langfuse import observe, get_client
    
    class LangfuseContextWrapper:
        def __init__(self):
            self.client = get_client()

        def update_current_trace(self, **kwargs: Any) -> None:
            self.client.update_current_trace(**kwargs)

        def update_current_observation(self, **kwargs: Any) -> None:
            # langfuse v3 client uses update_current_generation and update_current_span
            if "usage_details" in kwargs:
                self.client.update_current_generation(**kwargs)
            else:
                self.client.update_current_span(**kwargs)

        def score_current_trace(self, name: str, value: float) -> None:
            self.client.score_current_trace(name=name, value=value)

    langfuse_context = LangfuseContextWrapper()

except Exception:  # pragma: no cover
    def observe(*args: Any, **kwargs: Any):
        def decorator(func):
            return func
        return decorator

    class _DummyContext:
        def update_current_trace(self, **kwargs: Any) -> None:
            return None

        def update_current_observation(self, **kwargs: Any) -> None:
            return None

        def score_current_trace(self, name: str, value: float) -> None:
            return None

    langfuse_context = _DummyContext()


def tracing_enabled() -> bool:
    return bool(os.getenv("LANGFUSE_PUBLIC_KEY") and os.getenv("LANGFUSE_SECRET_KEY"))
