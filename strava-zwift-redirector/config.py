from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    # Source Strava API Configuration (for Zwift user)
    STRAVA_SOURCE_CLIENT_ID: str
    STRAVA_SOURCE_CLIENT_SECRET: str
    STRAVA_SOURCE_REFRESH_TOKEN: str

    # Target Strava API Configuration (for Strava user)
    STRAVA_TARGET_CLIENT_ID: str
    STRAVA_TARGET_CLIENT_SECRET: str
    STRAVA_TARGET_REFRESH_TOKEN: str

    # Webhook Configuration
    STRAVA_WEBHOOK_CALLBACK_URL: str = "https://strava-zwift-redirector.vercel.app/strava-notification"
    WEBHOOK_TIMEOUT: int = 30  # seconds

    # Application Configuration
    WATTAGE_THRESHOLD: float = 100.0
    
    # Flask Configuration
    FLASK_ENV: str = "production"
    FLASK_DEBUG: bool = False
    
    # Logging Configuration
    LOG_LEVEL: str = "INFO"
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()
