from typing import Annotated

from fastapi import Depends

from src.repositories.users.abc import AbstractUserRepository
from src.services.user_service import UserService
from src.storage.sql import AbstractSQLAlchemyStorage


class Dependencies:
    _storage: AbstractSQLAlchemyStorage
    _user_repository: AbstractUserRepository

    @classmethod
    def get_user_service(cls):
        return UserService(cls._user_repository)

    @classmethod
    def set_storage(cls, storage: AbstractSQLAlchemyStorage):
        cls._storage = storage

    @classmethod
    def set_user_repository(cls, user_repository: AbstractUserRepository):
        cls._user_repository = user_repository

    @classmethod
    def get_user_repository(cls) -> AbstractUserRepository:
        return cls._user_repository


USER_SERVICE_DEPENDENCY = Annotated[UserService, Depends(Dependencies.get_user_service)]
