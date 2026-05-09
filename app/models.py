"""Pydantic models for the microservice."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ItemBase(BaseModel):
    """Base Item model."""
    name: str = Field(..., min_length=1, max_length=100, description="Item name")
    description: Optional[str] = Field(None, max_length=500, description="Item description")
    price: float = Field(..., gt=0, description="Item price in EUR")
    category: Optional[str] = Field(None, max_length=50, description="Item category")


class ItemCreate(ItemBase):
    """Model for creating a new item."""
    pass


class ItemUpdate(BaseModel):
    """Model for updating an existing item."""
    name: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    price: Optional[float] = Field(None, gt=0)
    category: Optional[str] = Field(None, max_length=50)


class Item(ItemBase):
    """Complete Item model with ID."""
    id: int
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    """Base User model."""
    username: str = Field(..., min_length=3, max_length=50, description="Username")
    email: EmailStr = Field(..., description="Email address")
    full_name: Optional[str] = Field(None, max_length=100, description="Full name")


class UserCreate(UserBase):
    """Model for creating a new user."""
    password: str = Field(..., min_length=8, description="Password")


class UserUpdate(BaseModel):
    """Model for updating an existing user."""
    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    is_active: Optional[bool] = None


class User(UserBase):
    """Complete User model with ID."""
    id: int
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True
