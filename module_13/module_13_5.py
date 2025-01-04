from aiogram import Bot, Dispatcher, executor, types
import asyncio
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


TOKEN=""
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
kb = ReplyKeyboardMarkup()
button = KeyboardButton(text='Информация', resize_keyboard=True)
button2 = KeyboardButton(text='Рассчитать', resize_keyboard=True)
kb.add(button)
kb.add(button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("Привет, я бот помогающий твоему здоровью.", reply_markup=kb)

@dp.message_handler(text='Информация')
async def send_info(message: types.Message):
    await message.answer('Я помогаю тебе рассчитать норму калорий.', reply_markup=button)


@dp.message_handler(text='Рассчитать')
async def set_age(message, state):
    await message.answer('Введите свой возраст: ', reply_markup=button2)
    await UserState.age.set()

@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    await UserState.growth.set()
    await message.answer('Введите свой рост: ')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    await UserState.weight.set()
    await message.answer('Введите свой вес: ')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    calories = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) - 161
    await message.answer(f'Ваша норма калорий: {calories}')
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
