from __future__ import annotations

import time
import uuid

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from structlog.contextvars import bind_contextvars, clear_contextvars


class CorrelationIdMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
       # 1. Clear contextvars để tránh rò rỉ dữ liệu giữa các request song song
        clear_contextvars()
        # 2. Lấy x-request-id từ header hoặc tự sinh mới nếu không có
        correlation_id = request.headers.get("x-request-id")
        if not correlation_id:
            correlation_id = f"req-{uuid.uuid4().hex[:8]}"
        
        # 3. Liên kết correlation_id vào structlog contextvars
        bind_contextvars(correlation_id=correlation_id)
        
        request.state.correlation_id = correlation_id
        
        # 4. Tính toán thời gian xử lý phản hồi
        start = time.perf_counter()
        response = await call_next(request)
        
        # 5. Ghi các tham số vào response header để trả về client
        response.headers["x-request-id"] = correlation_id
        response.headers["x-response-time-ms"] = f"{(time.perf_counter() - start) * 1000:.2f}"
        
        return response
