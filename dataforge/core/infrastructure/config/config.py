import os

class Settings:
    DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://user:password@localhost/dataforge_db")

settings = Settings()
