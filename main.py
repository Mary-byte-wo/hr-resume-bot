import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден! Добавь его в Environment Variables на Render")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Пришли мне резюме (PDF или DOC), я сохраню и спрошу категорию позже 😊")

@dp.message(F.document)
async def handle_document(message: types.Message):
    kb = [[types.KeyboardButton(text="Пока просто тестирую приём файлов")]]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer(
        f"Получил файл: {message.document.file_name}\n"
        f"Размер: {message.document.file_size // 1024} КБ\n\n"
        "Бот живой и работает 24/7! 🚀\n"
        "Скоро добавлю Google Таблицы и кнопки категорий",
        reply_markup=keyboard
    )

@dp.message()
async def echo(message: types.Message):
    await message.answer("Я уже работаю! Жди полную версию с таблицей через 10 минут 😎")

async def main():
    logging.basicConfig(level=logging.INFO)
    print("Бот запущен и готов к работе!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
