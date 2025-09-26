import asyncio
import io
import csv
import logging

import aiohttp
from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils import markdown
from aiogram.enums import ParseMode, ChatAction
from aiogram.client.bot import DefaultBotProperties
from aiogram.utils.chat_action import ChatActionSender
from magic_filter import RegexpMode

from settings import settings

bot = Bot(
    token=settings.bot_token,
    # default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://www.citypng.com/public/uploads/preview/hd-python-logo-symbol-transparent-png-735811696257415dbkifcuokn.png"
    await message.answer(
        text=f"{markdown.hide_link(url=url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
    )


@dp.message(Command("help", prefix="/!%"))
async def handle_help(message: types.Message):
    text = markdown.text(
        markdown.markdown_decoration.quote("I am {echo} bot."),
        markdown.text(
            "Send me",
            markdown.markdown_decoration.bold(
                markdown.text(
                    markdown.underline("literally"),
                    "any",
                ),
            ),
            markdown.markdown_decoration.quote("message!"),
        ),
        sep="\n",
    )
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)


@dp.message(Command("code"))
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


@dp.message(Command("pic"))
async def handle_command_pic(message: types.Message):
    url = "https://images.unsplash.com/photo-1519451241324-20b4ea2c4220?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_PHOTO,
    )
    await message.reply_photo(
        photo=url,
    )


@dp.message(Command("file"))
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


@dp.message(Command("text"))
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


@dp.message(Command("csv"))
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
    file = io.BytesIO()  # just bytes
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


@dp.message(Command("pic_file"))
async def send_pic_file_buffered(message: types.Message):
    await message.bot.send_chat_action(
        chat_id=message.chat.id,
        action=ChatAction.UPLOAD_DOCUMENT,
    )
    # action_sender = ChatActionSender(
    #     bot=message.bot,
    #     chat_id=message.chat.id,
    #     action=ChatAction.UPLOAD_DOCUMENT,
    # )
    # async with action_sender:
    #     await send_big_file(message)
    #       or
    async with ChatActionSender.upload_document(
        bot=message.bot,
        chat_id=message.chat.id,
    ):
        await send_big_file(message)


#  Without magic-filter:
#
# def is_photo(message: types.Message):
#     return message.photo
#
#
# @dp.message(is_photo)
#
#      or
#
# @dp.message(lambda message: message.photo)


@dp.message(F.photo, ~F.caption)
async def handle_photo_wo_caption(message: types.Message):
    caption = "I can't see, sorry. Could you describe please?"
    await message.reply_photo(
        photo=message.photo[-1].file_id,
        caption=caption,
    )


@dp.message(F.photo, F.caption.contains("please"))
async def handle_photo_with_please_caption(message: types.Message):
    await message.reply("Don't beg me.")


any_media_filter = F.document | F.photo | F.video


@dp.message(any_media_filter, ~F.caption)
async def handle_any_media_without_caption(message: types.Message):
    if message.document:
        await message.reply_document(
            document=message.document.file_id,
        )
    elif message.video:
        await message.reply_video(
            video=message.video.file_id,
        )
    else:
        await message.reply("I can't see.")


@dp.message(any_media_filter, F.caption)
async def handle_any_media_with_caption(message: types.Message):
    await message.reply(f"Something is on media. Your text: {message.caption!r}")


@dp.message(F.from_user.id.in_({33, 339845222}), F.text == "secret")
async def secret_admin_message(message: types.Message):
    await message.reply("Hi admin!")


@dp.message(F.text.regexp(r"(\d+)", mode=RegexpMode.FINDALL).as_("code"))
async def handle_code(message: types.Message, code: list[str]):
    await message.reply(f"Your code: {code}")


@dp.message()
async def echo_message(message: types.Message):

    await message.answer(
        text="Wait a second...",
        parse_mode=None,
    )
    if message.sticker:
        await message.bot.send_chat_action(
            chat_id=message.chat.id,
            action=ChatAction.CHOOSE_STICKER,
        )
        await asyncio.sleep(2)
    # if message.text:
    #     await message.answer(
    #         text=message.text,
    #         entities=message.entities,
    #         parse_mode=None,
    #     )
    #     return
    try:
        # telegram side
        await message.copy_to(chat_id=message.chat.id)

        # aiogram side
        # await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.reply(text="Somthing new =)")


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
