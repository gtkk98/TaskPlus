import os
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker, declarative_base
from dotenv import load_dotenv

# Load secrets from the .env file
load_dotenv()

# Get the URL
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database model
Base = declarative_base()

# Dependency to get the database session in our routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()