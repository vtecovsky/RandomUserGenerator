from abc import ABC, abstractmethod

from src.schemas.users import User


class AbstractUserRepository(ABC):
    @abstractmethod
    async def setup_users(self, users: list[User]):
        ...

    @abstractmethod
    async def get_random_users(self, ids: list[int]):
        ...
