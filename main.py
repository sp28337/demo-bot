import asyncio
import logging
from sys import prefix

from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, types, F
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
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
