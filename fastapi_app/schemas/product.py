"""Module defining Pydantic schemas for product-related operations."""

from pydantic import ConfigDict, Field

from .base import BaseSchema


class ProductBase(BaseSchema):
    artikul: int

    model_config = ConfigDict(from_attributes=True)


class ProductRead(ProductBase):
    """Pydantic schema representing a columnist."""

    name: str
    price: int
    rating: int
    total_quantity: int
