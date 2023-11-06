__all__ = ["router"]

from fastapi import APIRouter

router = APIRouter(prefix="/api/v1/users", tags=["Users"])

import src.api.users.routes  # noqa: E402, F401
