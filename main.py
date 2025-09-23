import asyncio
import logging

from aiogram.filters import CommandStart, Command
from aiogram import Bot, Dispatcher, types
from aiogram.utils import markdown
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties
from settings import settings

bot = Bot(
    token=settings.bot_token,
    default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN_V2),
)
dp = Dispatcher()


@dp.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://png.pngtree.com/png-vector/20250227/ourlarge/pngtree-friendly-ai-robot-waving-with-a-smile-png-image_15607893.png"
    await message.answer(
        text=f"{markdown.hide_link(url=url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
    )


@dp.message(Command("help"))
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
    await message.answer(text=text)


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
    await message.answer(text=text)


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
