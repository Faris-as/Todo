"""
Pydantic Schemas for Request/Response validation
These define the shape of data going in and out of our API
"""
from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

class TodoBase(BaseModel):
    """Base schema common fields"""
    title: str = Field(..., min_length=1, max_length=200, description="Title of the todo")
    description: Optional[str] = Field(None, max_length=1000, description="Description of the todo")

class TodoCreate(TodoBase):
    """Schema for creating a new todo"""
    pass

class TodoUpdate(BaseModel):
    """Schema for updating a todo (all fields optional)"""
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = Field(None, max_length=1000)
    completed: Optional[bool] = None
    
class TodoResponse(BaseModel):
    """Schema for todo response (includes database fields)"""
    id: int
    completed: bool
    created_at: datetime
    updated_at: Optional[datetime]
    
    class Config:
        from_attributes = True  # Allows creating from ORM models
        