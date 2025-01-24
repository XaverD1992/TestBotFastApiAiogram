from fastapi import HTTPException, status
from pydantic import ValidationError
from typing import Any
from fastapi_app.schemas.product import ProductRead


def validate_product(product: dict[str, Any]):
    try:
        product = ProductRead.model_validate(product)
    except ValidationError:
        raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Ошибка валидации при получении данных от стороннего апи.",
    )
