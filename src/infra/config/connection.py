from typing import AsyncGenerator
from os import getenv
from dotenv import load_dotenv

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

load_dotenv()


SQLALCHEMY_DATABASE_URL = getenv("DATABASE_URL")


def create_database_engine(connection_string: str):
    """Create database async engine function"""

    return create_async_engine(connection_string)


async def get_db() -> AsyncGenerator:
    """Get database session to query"""

    engine = create_database_engine(SQLALCHEMY_DATABASE_URL)

    session = sessionmaker(
        engine, expire_on_commit=True, future=True, class_=AsyncSession
    )

    async with session() as session:
        try:
            yield session
            await session.commit()

        except SQLAlchemyError as sql_alchemy_exc:
            await session.rollback()
            raise sql_alchemy_exc

        except HTTPException as http_exc:
            await session.rollback()
            raise http_exc

        finally:
            await session.close()
