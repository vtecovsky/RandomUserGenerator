from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.users.abc import AbstractUserRepository
from src.storage.sql import AbstractSQLAlchemyStorage
from src.storage.sql.models import Currency


class SqlUserRepository(AbstractUserRepository):
    storage: AbstractSQLAlchemyStorage

    def __init__(self, storage: AbstractSQLAlchemyStorage):
        self.storage = storage

    def _create_session(self) -> AsyncSession:
        return self.storage.create_session()

    async def some_func(self):
        async with self._create_session() as session:
            query = select(Currency.name)
            selected_obj = await session.scalar(query)
            return selected_obj
