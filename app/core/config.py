from pydantic import BaseSettings

class Settings(BaseSettings):
    # Define your application settings here
    app_name: str = "MS Reactor API"
    environment: str = "development"
    debug: bool = True

    class Config:
        env_file = ".env"

settings = Settings()