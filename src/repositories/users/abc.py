from abc import ABC, abstractmethod

from src.schemas.users import RandomUser


class AbstractUserRepository(ABC):
    @abstractmethod
    async def setup_users(self, users: list[RandomUser]):
        ...

    @abstractmethod
    async def get_random_users(self, ids: list[int]):
        ...

    @abstractmethod
    async def are_users_setup(self):
        ...
