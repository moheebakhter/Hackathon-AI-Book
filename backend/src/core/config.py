from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    OPENAI_API_KEY: str
    QDRANT_URL: str
    QDRANT_API_KEY: str
    DATABASE_URL: str
    QDRANT_COLLECTION_NAME: str = "humanoid-robotics-book"
    EMBEDDING_MODEL: str = "text-embedding-3-small"
    COMPLETION_MODEL: str = "gpt-4o"


settings = Settings()
