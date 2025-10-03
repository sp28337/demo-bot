import asyncio
import io
import csv

import aiohttp
from aiogram.filters import Command
from aiogram import Bot, types, Router
from aiogram.utils import markdown
from aiogram.enums import ParseMode, ChatAction
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.chat_action import ChatActionSender

from keyboards.inline_keyboards.actions_kb import build_actions_keyboard
from keyboards.inline_keyboards.shop_kb import build_shop_keyboarb
from settings import settings

bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)

router = Router(name=__name__)


@router.message(Command("code"))
async def handle_command_code(message: types.Message):
    text = markdown.text(
        "Here's Python code:",
        "",
        markdown.markdown_decoration.pre_language(
            markdown.text(
                "print('Hello World!')", "\n", "def foo():\n    return 'bar'"
            ),
            language="python",
        ),
        sep="\n",
    )
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)


@router.message(Command("pic"))
async def handle_command_pic(message: types.Message):
    url = "https://images.unsplash.com/photo-1519451241324-20b4ea2c4220?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    await message.reply_photo(
        photo=url,
    )


@router.message(Command("file"))
async def handle_command_file(message: types.Message):
    file_path = "/home/sp28337/projects/telegram/sp28337_bot/public/images/IMG_2063.jpg"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    await message.reply_document(
        document=types.FSInputFile(
            path=file_path,
            filename="scrub.jpg",
        )
    )


@router.message(Command("text"))
async def handle_command_text(message: types.Message):
    file = io.StringIO()
    file.write("Hello Pattaya!\n")
    file.write("I'm coming very soon!")
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="text.txt",
        ),
    )


@router.message(Command("csv"))
async def handle_command_csv(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.TYPING,
    )

    file = io.StringIO()
    csv_writer = csv.writer(file)
    csv_writer.writerows(
        [
            ["Name", "Age", "City"],
            ["John Smith", "28", "New York"],
            ["Jane Doe", "23", "Los Angeles"],
            ["Pavel Tarakanov", "31", "Pattaya"],
        ]
    )
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode("utf-8"),
            filename="people.csv",
        ),
    )


async def send_big_file(message: types.Message):
    await asyncio.sleep(7)
    file = io.BytesIO()
    url = "https://images.unsplash.com/photo-1519451241324-20b4ea2c4220?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result_bytes = await response.read()

    file.write(result_bytes)
    await message.reply_document(
        document=types.BufferedInputFile(
            # file=result_bytes,
            file=file.getvalue(),
            filename="big-pic.jpg",
        )
    )


@router.message(Command("pic_file"))
async def send_pic_file_buffered(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    async with ChatActionSender.upload_document(
        bot=message.bot,
        chat_id=message.chat.id,
    ):
        await send_big_file(message)


@router.message(Command("actions", prefix="!/%"))
async def send_actions_message_with_kb(message: types.Message):
    await message.answer(
        text="Your actions:",
        reply_markup=build_actions_keyboard(),
    )


@router.message(Command("shop", prefix="!/%"))
async def send_actions_message_with_kb(message: types.Message):
    await message.answer(
        text="Your shop actions:",
        reply_markup=build_shop_keyboarb(),
    )
