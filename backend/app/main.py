"""
FastAPI Application Main File
This file contains:
1. FastAPI app initialization
2. CRUD operations (database functions)
3. REST API endpoints

For beginners: Everything in one place makes it easier to understand
the flow from HTTP request → database operation → HTTP response
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List

from . import models
from .database import engine, get_db
from .router import crud

# Create database tables 
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI(
    title="Todo List API",
    description="A simple RESTAPI for managing todos",
    version="1.0.0",
)

# Enable CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(crud.app)

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
            "DELETE /todos/{id}": "Delete a todo",
                    }
        }
