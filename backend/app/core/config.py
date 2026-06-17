from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application configuration loaded from environment / .env file."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Database
    database_url: str = "postgresql+psycopg://admissions:admissions@localhost:5432/admissions"

    # OpenAI
    openai_api_key: str = ""
    embedding_model: str = "text-embedding-3-small"
    embedding_dim: int = 1536
    chat_model: str = "gpt-4o-mini"

    # Auth / JWT
    jwt_secret: str = "change-me-to-a-long-random-string"
    jwt_algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    # RAG storage
    faiss_dir: str = "./data/faiss"
    upload_dir: str = "./data/uploads"
    retrieval_top_k: int = 5
    relevance_threshold: float = 0.35
    chunk_size: int = 800
    chunk_overlap: int = 100

    # CORS
    cors_origins: list[str] = ["http://localhost:3000"]

    # First admin (used by seed_admin script)
    first_admin_email: str = "admin@example.com"
    first_admin_password: str = "admin12345"
    first_admin_name: str = "Administrator"

    @field_validator("cors_origins", mode="before")
    @classmethod
    def _split_cors(cls, value: object) -> object:
        """Allow CORS_ORIGINS to be a comma-separated string in the env file."""
        if isinstance(value, str):
            return [origin.strip() for origin in value.split(",") if origin.strip()]
        return value


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
