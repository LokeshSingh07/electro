from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional
from decimal import Decimal


class ProductBase(BaseModel):
    name: str
    description: str
    price: Decimal
    stock: int
    brand: Optional[str] = None
    category_id: Optional[int] = None


class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[Decimal] = None
    stock: Optional[int] = None
















