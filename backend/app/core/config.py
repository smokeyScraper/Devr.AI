import os
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    # API Keys
    gemini_api_key: str = os.getenv("GEMINI_API_KEY", "")
    tavily_api_key: str = os.getenv("TAVILY_API_KEY", "")
    github_token: str = os.getenv("GITHUB_TOKEN", "")
    discord_bot_token: str = os.getenv("DISCORD_BOT_TOKEN", "")

    # TODO: Add DB configuration
    # Database
    # Supabase
    # Weaviate

    # Agent Configuration
    devrel_agent_model: str = "gemini-2.0-flash"
    github_agent_model: str = "gemini-2.0-flash"
    agent_timeout: int = 30
    max_retries: int = 3

    class Config:
        env_file = ".env"


settings = Settings()
