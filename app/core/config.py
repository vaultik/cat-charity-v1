from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_title: str = 'QRKot'
    description: str = 'Charity Project...'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'

    model_config = SettingsConfigDict(env_file='.env')


settings = Settings()
