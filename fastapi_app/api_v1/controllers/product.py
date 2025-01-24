from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from fastapi_app.api_v1.schedule_task import collect_data
from fastapi_app.api_v1.validators import validate_product
from fastapi_app.core.db import get_async_session
from fastapi_app.core.http_client import wb_client
from fastapi_app.crud.product import get_product, update_product, create_product
from fastapi_app.schemas.product import ProductRead, ProductBase

product_router = APIRouter()


@product_router.post("/products", response_model=ProductRead)
async def create_or_update_product(product_in: ProductBase, session: AsyncSession = Depends(get_async_session)):
    product = await wb_client.get_product(product_in.artikul)
    validate_product(product)
    existing_product = await get_product(session, product["artikul"])
    print(existing_product)
    if existing_product:
        return await update_product(session, product, existing_product)
    return await create_product(session, product)


@product_router.get("/subscribe/{artikul}")
async def create_or_update_product(artikul: int, session: AsyncSession = Depends(get_async_session)):
    from fastapi_app.main import scheduler
    trigger = IntervalTrigger(seconds=15)
    scheduler.add_job(jobstore='redis', func=collect_data, trigger=trigger, args=[artikul, session])
    scheduler.start()
    return {"message": "Сбор данных запущен"}

