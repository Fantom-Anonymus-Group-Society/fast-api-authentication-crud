from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    db_url: str = Field(..., env='DATABASE_URL')
    secret_key: str = Field(..., env='SECRET_KEY')
    algorithm: str = Field(..., env='ALGORITHM')
    media_dir_name: str = Field(..., env='MEDIA_DIR_NAME')
    file_name_length: str = Field(..., env="FILE_NAME_LENGTH")


env = Settings()
