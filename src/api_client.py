import logging
import time
from typing import Any

import requests

LOGGER = logging.getLogger(__name__)


class ApiClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})

    def set_bearer_token(self, token: str) -> None:
        self.session.headers.update({"Authorization": f"Bearer {token}"})

    def request(self, method: str, path: str, **kwargs: Any) -> requests.Response:
        started = time.perf_counter()
        response = self.session.request(
            method=method,
            url=f"{self.base_url}{path}",
            timeout=self.timeout,
            **kwargs,
        )
        elapsed_ms = (time.perf_counter() - started) * 1000
        response.elapsed_ms = elapsed_ms
        LOGGER.info("%s %s -> %s (%.0f ms)", method, path, response.status_code, elapsed_ms)
        return response

    def get(self, path: str, **kwargs: Any) -> requests.Response:
        return self.request("GET", path, **kwargs)

    def post(self, path: str, **kwargs: Any) -> requests.Response:
        return self.request("POST", path, **kwargs)
