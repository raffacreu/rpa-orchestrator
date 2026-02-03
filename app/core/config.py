from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str ="RPA Orchestrator"
    DATABASE_URL: str ="sqlite:///./rpa.db"

    class Config:
        env_file = ".env"

settings = Settings()