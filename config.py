from dataclasses import dataclass
import os
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_name: str = os.getenv("APP_NAME", "AI WhatsApp Bot")
    model_name: str = os.getenv("MODEL_NAME", "microsoft/DialoGPT-small")
    max_new_tokens: int = int(os.getenv("MAX_NEW_TOKENS", "60"))
    temperature: float = float(os.getenv("TEMPERATURE", "0.8"))


settings = Settings()
