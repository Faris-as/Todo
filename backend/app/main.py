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

@app.get("/", tags=["root"])
def root():
    return {
        "message": "Welcome to Todo List API",
        "docs": "/docs",
        "endpoints": {
            "GET /todos": "Get all todos",
            "GET /todos/{id}": "Get a specific todo",
            "POST /todos": "Create a new todo",
            "PUT /todos/{id}": "Update a todo",
            "DELETE /todos/{id}": "Delete a todo"
                    }
        }



@app.get("/todos", response_model=List[schemas.TodoResponse])
def read_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    Get all todos from database with pagination
    - skip: How many records to skip (for pagination)
    - limit: Maximum number of records to return
    """
    return db.query(models.Todo).offset(skip).limit(limit).all()


@app.get("/todo/{todo_id}")
def read_todo(db: Session = Depends(get_db), todo_id: int):
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
    