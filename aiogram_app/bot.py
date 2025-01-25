import asyncio
import json
import os

from aiohttp import ClientSession
from dotenv import load_dotenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = [
        [types.KeyboardButton(text="Получить данные по товару")],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)
    await message.answer("Привет! Нажмите кнопку ниже, чтобы получить данные по товару.", reply_markup=keyboard)


@dp.message(F.text.lower() == "получить данные по товару")
async def with_puree(message: types.Message):
    await message.answer("Введите артикул товара")


@dp.message(lambda message: message.text.isdigit())
async def process_product_code(message: types.Message):
    artikul = str(message.text)
    async with ClientSession() as session:
        async with session.post("http://backend:8000/api/v1/products", json={"artikul": artikul}
                ) as response:
            data = await response.json()

    await message.answer(json.dumps(data, indent=4, ensure_ascii=False,))


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
