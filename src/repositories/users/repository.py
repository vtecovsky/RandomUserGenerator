from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.repositories.users.abc import AbstractUserRepository
from src.schemas.users import User
from src.storage.sql import AbstractSQLAlchemyStorage
from src.storage.sql.models import User as UserModel


class SqlUserRepository(AbstractUserRepository):
    storage: AbstractSQLAlchemyStorage

    def __init__(self, storage: AbstractSQLAlchemyStorage):
        self.storage = storage

    def _create_session(self) -> AsyncSession:
        return self.storage.create_session()

    async def setup_users(self, users: list[User]):
        async with self._create_session() as session:
            users_data = [
                {
                    "fullname": user.fullname,
                    "gender": user.gender,
                    "age": user.age,
                    "address": user.address,
                    "email": user.email,
                    "username": user.username,
                }
                for user in users
            ]
            query = insert(UserModel).values(users_data)
            await session.execute(query)
            await session.commit()
