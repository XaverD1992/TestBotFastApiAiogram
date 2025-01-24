"""Module defining the base model for SQLAlchemy declarative models."""

from sqlalchemy.orm import (
    DeclarativeBase, Mapped, declared_attr, mapped_column
)


class Base(DeclarativeBase):
    """Base class for declarative models.

    Attributes:
        id (Mapped[int]): Primary key column.
    """

    __abstract__ = True

    # id: Mapped[int] = mapped_column(
    #     primary_key=True,
    #     autoincrement=True,
    # )

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """Generate table name based on lowercase class name.

        Returns:
            str: The table name for the class.
        """
        return f"{cls.__name__.lower()}"