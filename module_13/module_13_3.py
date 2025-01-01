from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from kye import api
import asyncio
import os



bot = os.getenv(api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.answer("Я бот обратной связи для учёбы")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_messages(message: types.Message):
    await message.answer("Введите команду /start, для начала работы")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
