"""
Database Models (SQLAlchemy ORM)
These classes represent tables in our database
"""

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from .database import Base

class Todo(Base):
    """
    Todo Model - represents a todo item in the database
    
    Fields:
    - id: Unique identifier (Primary Key)
    - title: Todo title (required)
    - description: Todo description (optional)
    - completed: Whether the todo is completed
    - created_at: When the todo was created
    - updated_at: When the todo was last updated
    """
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False, index=True)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    