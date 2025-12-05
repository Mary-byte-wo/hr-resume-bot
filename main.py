from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F
import asyncio
import logging

import os
BOT_TOKEN = os.getenv("BOT_TOKEN")  

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Пришли мне резюме (PDF или DOC), я сохраню и спрошу категорию позже 😉")

@dp.message(F.document)
async def handle_document(message: types.Message):
    await message.answer(f"Получил файл: {message.document.file_name}\nРазмер: {message.document.file_size // 1024} КБ\n\nСкоро добавлю выбор категории и сохранение в таблицу!")

@dp.message()
async def echo(message: types.Message):
    await message.answer("Пока я просто тестовый бот. Скоро буду умным! 😎")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
