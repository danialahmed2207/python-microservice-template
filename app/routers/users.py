"""User CRUD operations."""

from typing import List

from fastapi import APIRouter, HTTPException, status

from app.database import db
from app.models import User, UserCreate, UserUpdate

router = APIRouter()


@router.get("/", response_model=List[User])
async def list_users(skip: int = 0, limit: int = 100):
    """List all users with pagination."""
    users = list(db.users.values())
    return users[skip : skip + limit]


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: int):
    """Get a specific user by ID."""
    if user_id not in db.users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    return db.users[user_id]


@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate):
    """Create a new user."""
    # Check if username already exists
    for existing_user in db.users.values():
        if existing_user.username == user.username:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Username '{user.username}' already exists"
            )
        if existing_user.email == user.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Email '{user.email}' already registered"
            )

    user_id = db.get_next_user_id()
    new_user = User(id=user_id, username=user.username, email=user.email, full_name=user.full_name)
    db.users[user_id] = new_user
    return new_user


@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate):
    """Update an existing user."""
    if user_id not in db.users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )

    existing_user = db.users[user_id]
    update_data = user_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(existing_user, field, value)

    return existing_user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(user_id: int):
    """Delete a user."""
    if user_id not in db.users:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with ID {user_id} not found"
        )
    del db.users[user_id]
    return None
