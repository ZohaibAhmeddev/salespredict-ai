from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME: str = "SalesPredict AI"
    App_VERSION: str = "1.0.0"
    DEBUG: bool= True
    FRONTEND_URL: str = "http://localhost:5173"

    model_config = SettingsConfigDict(
        env_file = ".env",
        env_file_encoding="utf-8",
        extra= "ignore"
    )

settings = Settings()