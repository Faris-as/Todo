"""
CRUD Operations (Create, Read, Update, Delete)
These functions handle database operations
"""

from sqlalchemy.orm import Session
from . import models, schemas

def get_todos(db: Session, skip: int = 0, limit: int = 100):
    """Get all todos with pagination"""
    return db.query(models.Todo).offset(skip).limit(limit).all()

def get_todo(db: Session, todo_id: int):
    """Get a single todo by ID"""
    return db.query(models.Todo).filter(models.Todo.id == todo.id).first()

def create_todo(db: Session, todo: schemas.TodoCreate):
    """Create a new todo"""
    db_todo = models.Todo(**todo.model_dump())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo: schemas.TodoUpdate):
    """Update an existing todo"""
    db_todo = get_todo(db, todo_id)
    if db_todo:
        update_data = todo.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_todo, field, value)
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int):
    """Delete a todo"""
    db_todo = get_todo(db, todo_id)    
    if db_todo:
        db.delete(db_todo)
        db.commit()
        return True
    return False