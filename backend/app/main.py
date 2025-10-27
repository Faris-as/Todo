"""
FastAPI Application Main File
This file contains:
1. FastAPI app initialization
2. CRUD operations (database functions)
3. REST API endpoints

For beginners: Everything in one place makes it easier to understand
the flow from HTTP request → database operation → HTTP response
"""

from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models, schemas
from .database import engine, get_db

# Create database tables 
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Todo List API",
    description="A simple RESTAPI for managing todos"
    version="1.0.0"
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ============================================================================
# CRUD OPERATIONS - Database Functions
# ============================================================================
# These functions handle direct database interactions using SQLAlchemy

def db_get_todos(db: Session, skip: int = 0, limit: int = 100):
    """
    Get all todos from database with pagination
    - skip: How many records to skip (for pagination)
    - limit: Maximum number of records to return
    """
    return db.query(models.Todo).offset(skip).limit(limit).all()

def db_get_todo(db: Session, todo_id: int):
    """
    Get a single todo by its ID
    Returns None if todo doesn't exist
    """
    return db.query(models.Todo).filter(models.Todo.id == todo_id).first()

def db_create_todo(db:Session, todo:schemas.TodoCreate):
    """
    Create a new todo in the database
    Steps:
    1. Convert Pydantic model to SQLAlchemy model
    2. Add to database session
    3. Commit the transaction
    4. Refresh to get the created ID
    """
    