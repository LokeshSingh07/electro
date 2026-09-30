from fastapi import Depends, HTTPException, status, Cookie
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.config.auth import decode_access_token
from app.config.db import get_db
from app.models.user import User


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_current_user(
    # token: str = Depends(oauth2_scheme), 
    session_id: str | None = Cookie(default=None),
    db:Session = Depends(get_db)
):
    #  if not session_id:
        # raise HTTPException( status_code=status.HTTP_401_UNAUTHORIZED, detail="Authentication required")

    # decode from token to get user detail
    # payload = decode_access_token(token)
    payload = decode_access_token(session_id)
    
    if not payload:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentails")


    # get user id from JWT
    user_id = payload.get("sub")
    if not user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    # Find user in database
    user = db.get(User, int(user_id))
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="User not found")

    return user


def require_admin(user: User = Depends(get_current_user)) -> User :
    if user.role != "admin":
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin access required")

    return user