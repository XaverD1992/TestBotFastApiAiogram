from aiohttp import ClientSession
from fastapi import HTTPException, status



class HTTPClient:
    def __init__(self):
        self._session = None

    async def initialize(self, base_url: str):
        self._session = ClientSession(
            base_url=base_url,
        )


class WB_HTTPClient(HTTPClient):

    async def get_product(self, artikul: int) -> dict:
        async with self._session.get(f"/cards/v1/detail?appType=1&curr=rub&dest=-1257786&spp=30&nm={artikul}") as resp:
            full_result = await resp.json()
            print(full_result)
            try:
                product_info = {
                    "name": full_result["data"]["products"][0]["name"],
                    "artikul": full_result["data"]["products"][0]["id"],
                    "price": full_result["data"]["products"][0]["priceU"],
                    "rating": full_result["data"]["products"][0]["rating"],
                    "total_quantity": full_result["data"]["products"][0]["totalQuantity"],
                }
            except:
                raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail=f"Ошибка валидации при получении данных от стороннего апи.",
                )
            return product_info


wb_client = WB_HTTPClient()

