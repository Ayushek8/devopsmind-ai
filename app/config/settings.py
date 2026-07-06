from pydantic_settings import BaseSettings
from pydantic import ConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "DevOpsMind AI"

    APP_VERSION: str = "1.0.0"

    ENVIRONMENT: str = "development"

    LLM_PROVIDER: str = "groq"

    GROQ_API_KEY: str = ""

    LOG_LEVEL: str = "INFO"

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()