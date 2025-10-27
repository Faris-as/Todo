"""
Database Connection Setup 
This file manages the connection to PostgreSQL database 	
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from .env import DATABASE_URL

# Create database engine
# echo = True will print all SQL queries (useful for learning)
engine = create_engine(DATABASE_URL, echo=True)

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for our database sessions
Base = declarative_base()

# Dependency to get database session
def get_db():
    """
    Generator function that yields a database session.
    Automatically closes the session when done
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
