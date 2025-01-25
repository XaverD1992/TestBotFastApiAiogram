from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):

    APP_TITLE: str = "fff"
    APP_DESCRIPTION: str = "fff"
    DB_HOST: str = "localhost"
    DB_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "postgres"
    API_V1_PREFIX: str = "/api/v1"

    @property
    def DATABASE_URL(self):
        """This method returns data source name(DSN) in string format."""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:"
            f"{self.POSTGRES_PASSWORD}@"
            f"{self.DB_HOST}:{self.DB_PORT}/{self.POSTGRES_DB}"
        )

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()