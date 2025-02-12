from pydantic_settings import BaseSettings, SettingsConfigDict


class ConfigBase(BaseSettings):
    model_config = SettingsConfigDict(
        env_file="./app/config/.env", env_file_encoding="utf-8", extra="ignore"
    )


class DataBaseConfig(ConfigBase):
    HOST: str
    PORT: int
    NAME: str
    USER: str
    PASSWORD: str
    model_config = SettingsConfigDict(env_prefix="DB_")


class FastApiConfig(ConfigBase):
    HOST: str
    PORT: int
    SECRET_KEY: str
    ALGORITHM: str
    model_config = SettingsConfigDict(env_prefix="FA_")