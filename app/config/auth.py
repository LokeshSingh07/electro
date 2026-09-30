from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError
from passlib.context import CryptContext
from app.config.env import settings

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)



# PASSWORD
def hash_password(passwod:str) -> str:
    return pwd_context.hash(passwod)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)




# ACCESS_TOKEN
def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire_at = datetime.now(timezone.utc) + timedelta(minutes=settings.access_token_secret_expiry)
    to_encode.update({"exp": expire_at})

    return jwt.encode(to_encode, settings.secret_key, algorithm=settings.algorithm)

def decode_access_token(data: str) -> dict | None:
    try:
        return jwt.decode(data, settings.secret_key, algorithms=settings.algorithm)
    except JWTError:
        return None



