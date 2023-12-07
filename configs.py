import os
import openai
from dotenv import load_dotenv


class AppConfig:
    PY_ENV = os.getenv("PY_ENV", "development")
    PORT = os.getenv("PORT", "8001")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
    SIFATUL_API_URL = os.getenv("SIFATUL_API_URL", None)

    @classmethod
    def prepare(cls):
        if cls.PY_ENV != "production":
            if not load_dotenv():
                raise EnvironmentError("Unable to load ENV")
        cls.PORT = os.getenv("PORT", "8001")
        cls.OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", None)
        cls.SIFATUL_API_URL = os.getenv("SIFATUL_API_URL", None)

        openai.api_key = cls.OPENAI_API_KEY
