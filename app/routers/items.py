"""Item CRUD operations."""

from typing import List

from fastapi import APIRouter, HTTPException, status

from app.database import db
from app.models import Item, ItemCreate, ItemUpdate

router = APIRouter()


@router.get("/", response_model=List[Item])
async def list_items(skip: int = 0, limit: int = 100):
    """List all items with pagination."""
    items = list(db.items.values())
    return items[skip : skip + limit]


@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    """Get a specific item by ID."""
    if item_id not in db.items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    return db.items[item_id]


@router.post("/", response_model=Item, status_code=status.HTTP_201_CREATED)
async def create_item(item: ItemCreate):
    """Create a new item."""
    item_id = db.get_next_item_id()
    new_item = Item(id=item_id, **item.model_dump())
    db.items[item_id] = new_item
    return new_item


@router.put("/{item_id}", response_model=Item)
async def update_item(item_id: int, item_update: ItemUpdate):
    """Update an existing item."""
    if item_id not in db.items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )

    existing_item = db.items[item_id]
    update_data = item_update.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(existing_item, field, value)

    return existing_item


@router.delete("/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_item(item_id: int):
    """Delete an item."""
    if item_id not in db.items:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Item with ID {item_id} not found"
        )
    del db.items[item_id]
    return None
