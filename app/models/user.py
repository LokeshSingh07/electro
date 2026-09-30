from sqlalchemy import Column, Integer, String, Boolean, Enum, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from app.config.db import Base
import enum


class UserRole(str, enum.Enum):
    admin = "admin"
    seller = "seller"
    customer = "customer"


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    role = Column(
        Enum("admin", "seller", "customer", name="user_role"),
        nullable=False,
        default="customer"
    )
    is_active       = Column(Boolean, default=False)
    is_verified     = Column(Boolean, default=False)
    created_at      = Column(DateTime, server_default=func.now())
    updated_at      = Column(DateTime, server_default=func.now(), onupdate=func.now())



    # relationship
    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user")
    carts = relationship("Cart", back_populates="user", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user", cascade="all, delete-orphan")
    seller = relationship("Product", back_populates="seller")