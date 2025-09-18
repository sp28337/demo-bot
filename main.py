import os
import asyncio
import logging

from aiogram.filters import CommandStart, Command
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types


load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

bot = Bot(token=bot_token)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    await message.answer(text=f"Hello, {message.from_user.full_name}")


@dp.message(Command("help"))
async def handle_help(message: types.Message):
    await message.answer(text="I am echo bot.\nSend me any message!")


@dp.message()
async def echo_message(message: types.Message):

    await message.answer(text="Wait a second...")
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Somthing new =)")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
