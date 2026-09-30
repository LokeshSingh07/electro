from fastapi import APIRouter, Depends, Response
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.config.db import get_db
from app.services.auth_service import signup_user, login_user
from app.schemas.user import UserCreate
from app.middlewares.security import get_current_user
from app.models.user import User


# router = APIRouter(
#     prefix="/auth",
#     tags=['Auth']
# )

router = APIRouter()



# ==================================================
# Signup
# ==================================================
@router.post("/signup", status_code=201)
def signup(
    user: UserCreate, 
    db: Session = Depends(get_db)
):
    return signup_user(user, db)





# ==================================================
# Login
# ==================================================
@router.post("/login", status_code=200)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
    res: Response = None
):
    return login_user(
        form_data=form_data,
        db = db,
        res = res
    )



@router.get("/me")
def get_me(user: User = Depends(get_current_user)):
    return {
        "id": user.id,
        "email": user.email,
        "full_name": user.full_name,
        "role": user.role
    }