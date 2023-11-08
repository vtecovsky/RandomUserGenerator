import random

from faker import Faker

from src.exceptions import InvalidQueryParam
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
        lastname = "_".join(name_parts[1:])
        return f"{firstname.lower()}_{lastname.lower()}@example.com"

    @staticmethod
    def __generate_unique_ints(n: int) -> list[int]:
        unique_nums = set()
        while len(unique_nums) < n:
            random_number = fake.random_int(min=0, max=1000)
            unique_nums.add(random_number)
        return list(unique_nums)

    async def __generate_random_users(self) -> list[User]:
        users: list[User] = []
        genders = ("F", "M")
        for _ in range(self.__max_unique_users):
            gender = random.choice(genders)
            fullname = UserService.__generate_fullname(gender)
            gender = gender
            age = random.randint(1, 114)
            address = fake.unique.address()
            email = UserService.__generate_email(fullname)
            username = fake.unique.user_name()
            user = User(
                gender=gender,
                fullname=fullname,
                age=age,
                address=address,
                email=email,
                username=username,
            )
            users.append(user)
        fake.clear()
        return users

    @staticmethod
    def validate_n(n):
        if n < 0 or n > 1000:
            raise InvalidQueryParam()

    async def setup_random_users(self):
        users = await self.__generate_random_users()
        await self.user_repo.setup_users(users)

    async def get_random_users(self, n: int):
        UserService.validate_n(n)
        unique_nums = UserService.__generate_unique_ints(n)
        return await self.user_repo.get_random_users(unique_nums)
