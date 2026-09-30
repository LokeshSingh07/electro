from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime, func, Enum
from sqlalchemy.orm import relationship
from app.config.db import Base
from enum import Enum as pyEnum

class OrderStatus(str, pyEnum):
    pending = "pending"
    shipped = "shipped"
    out_for_delivery = "out_for_delivery"
    cancelled = "cancelled"
    delivered = "delivered"


class Order(Base):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())
    status = Column(Enum(OrderStatus), default=OrderStatus.pending, nullable=False)
    price_at_purchase = Column(Float, nullable=False)


    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    address_id = Column(Integer, ForeignKey("address.id"), nullable=False)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)


    # relationship
    user    = relationship("User", back_populates="order")
    address = relationship("Address", back_populates="order")
    product = relationship("Product", back_populates="order")

    payment = relationship("Payment", back_populates="order")