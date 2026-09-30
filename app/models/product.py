from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, DateTime, func, CheckConstraint
from sqlalchemy.orm import relationship
from app.config.db import Base





class Product(Base):
    __tablename__ = "product"
    __table_args__ = (
        CheckConstraint("price >= 0", name="ck_product_price_positive"),
        CheckConstraint("stock > 0", name="ck_product_stock_non_negative"),
    )

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    stock = Column(Integer, default=0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now())

    seller_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)



    # relationship
    seller      = relationship("User", back_populates="seller")
    category    = relationship("Category", back_populates="product")
    images      = relationship("ProductImage", back_populates="product")
    reviews     = relationship("Review", back_populates="product")
    cart_items  = relationship("Cart", back_populates="product")
    order_items = relationship("Order", back_populates="product")





class ProductImage(Base):
    __tablename__ = "product_image"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    image_url = Column(String, nullable=False)
    is_primary = Column(Boolean, default=False)

    product = relationship("Product", back_populates="images")