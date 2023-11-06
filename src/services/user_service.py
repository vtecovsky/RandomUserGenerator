from src.repositories.users.abc import AbstractUserRepository
from src.schemas.users import User


class UserService:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo

    async def get_random_users(self, n: int):
        return await self.user_repo.some_func()

    def generate_random_users(self):
        users: list[User] = []
        ...

    def __generate_email(self):
        ...
