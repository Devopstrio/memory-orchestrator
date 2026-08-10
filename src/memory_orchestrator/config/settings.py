"""Settings."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    environment: str = "development"
    redis_url: str = "redis://localhost:6379/0"
    pg_dsn: str = "postgresql://postgres:postgres@localhost:5432/memorydb"
    neo4j_uri: str = "bolt://localhost:7687"
    neo4j_user: str = "neo4j"
    neo4j_password: str = "password"
    host: str = "0.0.0.0"
    port: int = 8080

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

def get_settings() -> Settings:
    return Settings()
