from pydantic_settings import BaseSettings
from functools import lru_cache


class settings(BaseSettings):
    DB_NAME: str
    DB_USERNAME: str
    DB_PASSWORD: str
    class Config:
        env_file: str = ".env"

@lru_cache
def get_settings() -> settings:
    return settings()