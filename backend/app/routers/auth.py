from fastapi import APIRouter, HTTPException, status, Depends
from ..schemas import UserRead, UserCreate
from ..database import SessionDep
from sqlmodel import select
from ..models import Users
from ..security import hash_password

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register", response_model=UserRead, status_code=201)
def register(session: SessionDep, user: UserCreate):
    statement = select(Users).where(Users.email == user.email)
    existing_user = session.exec(statement).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, 
            detail=f"User with {user.email} already exist."  
        )
        
    db_user = Users(
        email=user.email,
        hashed_password=hash_password(user.password)
    )
    
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    
    return db_user