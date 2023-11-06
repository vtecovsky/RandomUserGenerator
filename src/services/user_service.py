from src.repositories.user.abc import AbstractUserRepository


class UserService:
    def __init__(self, user_repo: type[AbstractUserRepository]):
        self.user_repo = user_repo


