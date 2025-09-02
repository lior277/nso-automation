from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    base_url: str = os.getenv("BASE_URL", "https://reqres.in")
    timeout: int = int(os.getenv("TIMEOUT", "10"))

settings = Settings()
