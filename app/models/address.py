from sqlalchemy import Column, Integer, String, Enum, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from app.config.db import Base



class Address(Base):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    label = Column(Enum("home", "work", "other", name="address_label"), nullable=False)
    line1 = Column(String, nullable=False)
    line2 = Column(String)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    postal_code = Column(String, nullable=False)
    country = Column(String, nullable=False)
    is_default = Column(Boolean, default=False)

    # relationship
    user    = relationship("User", back_populates="address")
    order   = relationship("Order", back_populates="address")