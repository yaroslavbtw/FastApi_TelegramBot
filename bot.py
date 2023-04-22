import os

from aiogram import Dispatcher, Bot, types
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get("TOKEN")

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.answer(f"Hello, <b>{ message.from_user.full_name}</b>! 😘\n\nI'm a test bot. "
                         f"My developer is https://github.com/yaroslavbtw. Follow his account to learn about updates!")
