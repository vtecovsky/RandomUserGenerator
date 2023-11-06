from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.user.abc import AbstractUserRepository
from src.storage.sql import AbstractSQLAlchemyStorage


class SqlUserRepository(AbstractUserRepository):
    storage: AbstractSQLAlchemyStorage

    def __init__(self, storage: AbstractSQLAlchemyStorage):
        self.storage = storage

    def _create_session(self) -> AsyncSession:
        return self.storage.create_session()
