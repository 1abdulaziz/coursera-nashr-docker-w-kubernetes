import os

class Config():
    SQLALCHEMY_DATABASE_URI = "postgresql://" + os.getenv("POSTGRES_USER") + ":" + os.getenv("POSTGRES_PASSWORD") + "@" + os.getenv("POSTGRES_HOST") + ":" + os.getenv("POSTGRES_PORT") + "/" + os.getenv("POSTGRES_DB")