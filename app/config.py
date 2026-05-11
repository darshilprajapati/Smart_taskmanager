import os

class Config:

    SECRET_KEY = os.getenv(
        "SECRET_KEY",
        "secret"
    )

    SQLALCHEMY_DATABASE_URI = os.getenv(
        "postgresql://neondb_owner:YOUR_PASSWORD@ep-dark-cherry-aq84jh37-pooler.c-8.us-east-1.aws.neon.tech/neondb?sslmode=require"
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False