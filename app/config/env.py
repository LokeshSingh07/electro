from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


SQLALCHEMY_DATABASE_URL = os.getenv("SQLALCHEMY_DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")
SECRET_EXPIRY = os.getenv("SECRET_EXPIRY")
ORIGIN = os.getenv("ORIGIN")



class Settings(BaseSettings):
    database_url: str = SQLALCHEMY_DATABASE_URL
    origin: str = ORIGIN
    secret_key: str = SECRET_KEY
    algorithm: str = "HS256"
    access_token_secret_expiry: int = SECRET_EXPIRY

    class config:
        env_file = ".env"


settings = Settings()