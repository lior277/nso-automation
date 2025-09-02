# src/core/http_client.py
import requests
from requests import Response
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

class Http:
    """Lightweight HTTP wrapper with retries and default headers."""
    def __init__(self, timeout: float = 20.0):
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": (
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/98.0.4758.82 Safari/537.36"
            ),
            "Accept": "application/json",
        })

        retry = Retry(
            total=3,
            backoff_factor=0.2,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "HEAD", "OPTIONS"],
        )
        adapter = HTTPAdapter(max_retries=retry)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)

    def get(self, url: str) -> Response:
        resp = self.session.get(url, timeout=self.timeout)
        resp.raise_for_status()
        return resp

    def post(self, url: str, json: object) -> Response:
        resp = self.session.post(url, json=json, timeout=self.timeout)
        resp.raise_for_status()
        return resp

    def put(self, url: str, json: object) -> Response:
        resp = self.session.put(url, json=json, timeout=self.timeout)
        resp.raise_for_status()
        return resp

    def patch(self, url: str, json: object) -> Response:
        resp = self.session.patch(url, json=json, timeout=self.timeout)
        resp.raise_for_status()
        return resp

    def delete(self, url: str, json: object = None) -> Response:
        resp = self.session.delete(url, json=json, timeout=self.timeout)
        resp.raise_for_status()
        return resp


def build_session(timeout: int = 10) -> requests.Session:
    return Http(timeout=timeout).session
