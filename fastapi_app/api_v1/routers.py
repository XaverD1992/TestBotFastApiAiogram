from fastapi import APIRouter

from fastapi_app.api_v1.controllers import product_router

router_v1 = APIRouter()

router_v1.include_router(
    product_router, prefix="", tags=["products"]
)