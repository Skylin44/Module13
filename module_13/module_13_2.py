from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from kye import api
import asyncio


bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    print("Привет, я бот помогающий твоему здоровью.")

@dp.message_handler()
async def all_messages(message: types.Message):
    print("Введите команду /start, для начала работы")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
    