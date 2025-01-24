"""Module defining the base schema for Pydantic models."""

from pydantic import BaseModel


class BaseSchema(BaseModel):
    """Base Pydantic schema allowing arbitrary types."""

    class Config:
        """Pydantic configuration for BaseSchema.

        Attributes:
            arbitrary_types_allowed (bool): Whether arbitrary types
                are allowed for the schema.
        """

        arbitrary_types_allowed = True