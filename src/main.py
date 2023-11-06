from fastapi import FastAPI

from src.api.dependencies import Dependencies
from src.api.routers import routers
from src.config import settings
from src.repositories.user.repository import SqlUserRepository
from src.storage.sql import PostgresSQLAlchemyStorage

app = FastAPI()


async def setup_repositories():
    storage = PostgresSQLAlchemyStorage.from_url(settings.DB_URL)
    currency_repository = SqlUserRepository(storage)


@app.on_event("startup")
async def startup_event():
    await setup_repositories()


for router in routers:
    app.include_router(router)
