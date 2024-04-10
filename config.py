from pydantic_settings import BaseSettings, SettingsConfigDict


class AppSettings(BaseSettings):
    BOT_TOKEN: str
    OWM_API_KEY: str

    model_config = SettingsConfigDict(env_file=".env")


Settings = AppSettings()
