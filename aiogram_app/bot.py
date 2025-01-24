import asyncio
import os

import aiohttp
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
    async with aiohttp.ClientSession() as session:
        async with session.get("https://backend:80/api/v1/products") as response:
            data = await response.json()
    await message.answer(data)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
