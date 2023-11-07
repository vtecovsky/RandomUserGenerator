import random

from faker import Faker

from src.repositories.users.abc import AbstractUserRepository
from src.schemas.users import User

fake = Faker()


class UserService:
    def __init__(self, user_repo: AbstractUserRepository):
        self.user_repo = user_repo
        self.__max_unique_users = 1000

    @staticmethod
    def __generate_fullname(gender: str) -> str:
        if gender == "F":
            return fake.unique.name_female()
        return fake.unique.name_male()

    @staticmethod
    def __generate_email(fullname: str) -> str:
        name_parts = fullname.split(" ")
        firstname = name_parts[0]
        lastname = " ".join(name_parts[1:])
        return f"{firstname.lower()}.{lastname.lower()}@example.com"

    async def __generate_random_users(self) -> list[User]:
        users: list[User] = []
        genders = ["F", "M"]
        for _ in range(self.__max_unique_users):
            gender = random.choice(genders)
            fullname = UserService.__generate_fullname(gender)
            gender = gender
            age = random.randint(1, 114)
            address = fake.unique.address()
            email = UserService.__generate_email(fullname)
            username = fake.unique.user_name()
            user = User(gender=gender, fullname=fullname, age=age, address=address, email=email, username=username)
            users.append(user)
        return users

    async def setup_random_users(self):
        users = await self.__generate_random_users()
        await self.user_repo.setup_users(users)
