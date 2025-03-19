 
from tortoise import Tortoise
import os 
DB_URL = os.getenv("db_url")

async def init_db():
    """Initialize the database connection."""
    await Tortoise.init(
        db_url=DB_URL,
        modules={"models": []}  # Import your models
    )
    await Tortoise.generate_schemas()  # Create tables if they don't exist

async def close_db():
    """Close the database connection."""
    await Tortoise.close_connections()

