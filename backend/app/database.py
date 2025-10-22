"""
Database Connection Setup 
This file manages the connection to PostgreSQL database 	
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Get database URL from environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://todouser:todopass@localhost:5432/tododb")

# Create database engine
# echo = True will print all SQL queries (useful for learning)
engine = create_engine(DATABASE_URL, echo=True)

# Create a SessionLocal class for database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

 