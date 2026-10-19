from fastapi import APIRouter
from ..security import CurrentUser
from ..schemas import UserRead

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get('/me')
def read_current_user(current_user: CurrentUser) -> UserRead:
    return current_user