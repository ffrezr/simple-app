from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from ...database import get_db
from .schemas import UserCreate, UserResponse, UserUpdate
from .services import create_user, get_users, get_user_by_id, update_user, delete_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user"""
    return create_user(db, user)

@router.get("/", response_model=List[UserResponse])
def get_users_endpoint(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all users with pagination"""
    return get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """Get a specific user by ID"""
    user = get_user_by_id(db, user_id)
    if user is None:
        from fastapi import HTTPException, status
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.put("/{user_id}", response_model=UserResponse)
def update_user_endpoint(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """Update a user"""
    return update_user(db, user_id, user_update)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    """Delete a user"""
    delete_user(db, user_id)
    return None
