from typing import List
from fastapi import status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from .. import models, schemas
from ..config.engine import get_db
from ..config.utils import hash_password

router = APIRouter(
    prefix="/v1/users",
    tags=["Users"]
)


@router.get("/", response_model=List[schemas.user.User])
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.user.User).all()
    return users


@router.get("/{user_id}", response_model=schemas.user.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(models.user.User).filter(models.user.User.id == user_id).first()
    check_if_exists(user, user_id)
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.user.User)
def create_user(user: schemas.user.UserCreate, db: Session = Depends(get_db)):
    hashed_password = hash_password(user.password)
    user.password = hashed_password
    new_user = models.user.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def check_if_exists(user, user_id):
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with {user_id} id was not found")
