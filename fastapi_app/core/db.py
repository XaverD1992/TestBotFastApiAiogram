"""
This module provides configurations for database connection.

"""

from fastapi import Depends
# from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from fastapi_app.core.config import settings
# from app.models.user import User


engine = create_async_engine(settings.DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(engine, class_=AsyncSession)


async def get_async_session():
    """Return session instance to interact with the database."""
    async with AsyncSessionLocal() as async_session:
        yield async_session