from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from fastapi_app.models.product import Product


async def get_product(session: AsyncSession, artikul: int) -> Product | None:
    return await session.get(Product, artikul)


async def create_product(session: AsyncSession, product: dict) -> Product:
    product = Product(**product)
    session.add(product)
    await session.commit()
    await session.refresh(product)
    return product


async def update_product(session: AsyncSession, product: dict, existing_product: Product):
    for name, value in product.items():
        setattr(existing_product, name, value)
    setattr(existing_product, "updated_at", func.now())
    await session.commit()
    return product
