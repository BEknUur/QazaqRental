import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    ALLOWED_ORIGINS = [
         "http://161.35.217.68"
    ]

settings = Settings()
