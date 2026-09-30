from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime


class UserCreate(BaseModel):
    email: str
    password: str
    full_name: str
    role: str

class UserRead(BaseModel):
    id: int
    email: EmailStr
    full_name: str
    role: str



class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

