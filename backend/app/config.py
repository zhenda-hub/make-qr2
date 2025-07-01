from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str
    
    model_config = SettingsConfigDict(case_sensitive=True)

settings = Settings()
