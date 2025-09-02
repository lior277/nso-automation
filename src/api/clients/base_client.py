# src/api/clients/base_client.py
from src.core.config import settings
from src.core.http_client import build_session

class BaseClient:
    def __init__(self, base_url: str | None = None, timeout: int | None = None):
        self.base_url = base_url or settings.base_url
        self.s = build_session(timeout or settings.timeout)

    def _url(self, path: str) -> str:
        return f"{self.base_url}{path}"
