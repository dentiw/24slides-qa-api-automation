import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("API_BASE_URL", "https://dummyjson.com").rstrip("/")
    username: str = os.getenv("API_USERNAME", "emilys")
    password: str = os.getenv("API_PASSWORD", "emilyspass")
    max_response_time_ms: int = int(os.getenv("MAX_RESPONSE_TIME_MS", "1000"))


settings = Settings()
