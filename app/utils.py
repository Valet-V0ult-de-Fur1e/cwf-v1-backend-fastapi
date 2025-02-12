from .config import FastApiConfig, DataBaseConfig

server_settings = FastApiConfig()
db_settings = DataBaseConfig()


def get_db_url():
    return (f"postgresql+asyncpg://{db_settings.USER}:{db_settings.PASSWORD}@"
            f"{db_settings.HOST}:{db_settings.PORT}/{db_settings.NAME}")

def get_server_data():
    return server_settings.HOST, server_settings.PORT


def get_auth_data():
    return {"secret_key": server_settings.SECRET_KEY, "algorithm": server_settings.ALGORITHM}