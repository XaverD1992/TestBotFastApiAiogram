from sqlalchemy import TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from .base import Base

class Product(Base):

    __tablename__ = "product_table"

    name: Mapped[str]
    artikul: Mapped[int] = mapped_column(unique=True, primary_key=True)
    price: Mapped[int]
    rating: Mapped[int]
    total_quantity: Mapped[int]
    updated_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        # onupdate=func.now(),
    )
