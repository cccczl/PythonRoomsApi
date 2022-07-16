from typing import Type, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException

from src.domain.usecases.users_usecases.find_user_by_id_collector import (
    FindUserByIdCollectorInterface,
)
from src.data.interfaces.users_repository import UsersRepositoryInterface


class FindUserByIdCollector(FindUserByIdCollectorInterface):
    """Find User By Id collector usecase"""

    def __init__(self, users_repository: Type[UsersRepositoryInterface]) -> None:
        self.__users_repository = users_repository

    async def find_user_by_id(self, db_session: AsyncSession, user_id: int) -> Dict:
        """
        Find user by id and return it
        :param  - db_session: ORM database session
                - user_id: User id to find
        :returns - Dictionary with user information
        """

        api_response = await self.__users_repository.get_user_by_id(db_session, user_id)

        if api_response is None:
            raise HTTPException(status_code=404, detail="User not found")

        return api_response
