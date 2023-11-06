from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    class Config:
        env_file = ".env.local"
        env_file_encoding = "utf-8"

    DB_URL: str


settings = Settings()
