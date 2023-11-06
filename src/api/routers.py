from src.api.users import router as users_router

routers = [users_router]

__all__ = ["routers", *routers]
