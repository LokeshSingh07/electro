from fastapi import HTTPException, Response 
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import select


from app.config.db import get_db
from app.schemas.user import UserCreate, Token
from app.config.auth import hash_password, verify_password, create_access_token, decode_access_token
from app.models.user import User





# ==================================================
# SignUp
# ==================================================
def signup_user(
    user: UserCreate,
    db:Session
):
    # check user already exist
    existing_user = db.execute(
        select(User).where(
            User.email == user.email
        )
    ).scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    db_user = User(
        full_name = user.full_name,
        email = user.email,
        password = hash_password(user.password),
        role= "customer"
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user





# ==================================================
# Login
# ==================================================
def login_user(form_data: OAuth2PasswordRequestForm, db: Session, res:Response):
    existing_user = db.execute(
            select(User).where(
                User.email == form_data.username
            )
        ).scalar_one_or_none()
    
    if not existing_user:
        raise HTTPException(status_code=400, detail="Email not registered")

    if not verify_password(form_data.password, existing_user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")

    payload = {
        "sub": str(existing_user.id),
        "email": str(existing_user.email),
        "role": str(existing_user.role)
    }

    token = create_access_token(payload)

    res.set_cookie(
        key="session_id",
        value=token,
        httponly=True,      # JS can't access it — prevents XSS token theft
        secure=True,         # only sent over HTTPS
        samesite="lax",      # CSRF protection
        max_age=3600          # expires in 1 hour
    )

    return {
        "access_token": token,
        "user": {
            "email": existing_user.email,
            "full_name": existing_user.full_name,
            "role": existing_user.role
        }
    }