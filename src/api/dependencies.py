from typing import Annotated

from fastapi import Depends

from src.repositories.user.repository import SqlUserRepository
from src.services.user_service import UserService


class Dependencies:

    @classmethod
    def user_service(cls):
        return UserService(SqlUserRepository)


USER_SERVICE_DEPENDENCY = Annotated[UserService, Depends(Dependencies.user_service)]
