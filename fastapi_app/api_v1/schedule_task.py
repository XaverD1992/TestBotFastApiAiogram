from fastapi_app.api_v1.validators import validate_product
from fastapi_app.core.http_client import wb_client
from fastapi_app.crud.product import get_product, update_product, create_product


async def collect_data(artikul, session):
    print("старт сбора")
    product = await wb_client.get_product(artikul)
    validate_product(product)
    existing_product = await get_product(session, product["artikul"])
    if existing_product:
        return await update_product(session, product, existing_product)
    return await create_product(session, product)
