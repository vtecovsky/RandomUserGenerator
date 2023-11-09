from src.api.dependencies import USER_SERVICE_DEPENDENCY
from src.api.users import router
from src.schemas.users import RandomUserResponse


@router.get("/", response_model=RandomUserResponse)
async def get_random_users(n: int, user_service: USER_SERVICE_DEPENDENCY):
    """Get N random users"""
    random_users = await user_service.get_random_users(n)
    return random_users
