import os

class Config():
    SQLALCHEMY_DATABASE_URI = "postgresql://" + os.environ['POSTGRES_USER'] + ":" + os.environ['POSTGRES_PASSWORD'] + "@" + os.environ['POSTGRES_HOST'] + ":" + os.environ['POSTGRES_PORT'] + "/" + os.environ['POSTGRES_DB']