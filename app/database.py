"""In-Memory Database for demo purposes.
In production, replace with PostgreSQL, MySQL, etc."""

from datetime import datetime
from typing import Dict, List, Optional

from app.models import Item, User


class Database:
    """Simple in-memory database."""

    def __init__(self):
        self.items: Dict[int, Item] = {}
        self.users: Dict[int, User] = {}
        self._item_counter = 0
        self._user_counter = 0

    def get_next_item_id(self) -> int:
        self._item_counter += 1
        return self._item_counter

    def get_next_user_id(self) -> int:
        self._user_counter += 1
        return self._user_counter


db = Database()


def init_db():
    """Initialize database with sample data."""
    # Add sample items
    sample_items = [
        Item(id=1, name="Laptop", description="Development laptop", price=1200.00, category="Electronics"),
        Item(id=2, name="Monitor", description="27\" 4K Display", price=400.00, category="Electronics"),
        Item(id=3, name="Desk Chair", description="Ergonomic office chair", price=350.00, category="Furniture"),
    ]
    for item in sample_items:
        db.items[item.id] = item
    db._item_counter = len(sample_items)

    # Add sample users
    sample_users = [
        User(id=1, username="danial", email="danial@example.com", full_name="Danial Ahmed", is_active=True),
        User(id=2, username="admin", email="admin@example.com", full_name="Admin User", is_active=True),
    ]
    for user in sample_users:
        db.users[user.id] = user
    db._user_counter = len(sample_users)
