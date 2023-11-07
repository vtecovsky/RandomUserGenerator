from fastapi import FastAPI

from src.api.dependencies import Dependencies
from src.api.routers import routers
from src.config import settings
from src.repositories.users.repository import SqlUserRepository
from src.storage.sql import PostgresSQLAlchemyStorage

app = FastAPI()


async def setup_dependencies():
    storage = PostgresSQLAlchemyStorage.from_url(settings.DB_URL)
    user_repository = SqlUserRepository(storage)
    Dependencies.set_storage(storage)
    Dependencies.set_user_repository(user_repository)
    user_service = Dependencies.get_user_service()

    await user_service.setup_random_users()

    # await storage.drop_all()
    # await storage.create_all()


@app.on_event("startup")
async def startup_event():
    await setup_dependencies()


for router in routers:
    app.include_router(router)
