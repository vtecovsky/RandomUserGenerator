from src.api.dependencies import USER_SERVICE_DEPENDENCY
from src.api.users import router


@router.get("")
async def get_random_users(n: int, user_service: USER_SERVICE_DEPENDENCY):
    return await user_service.get_random_users(n)
