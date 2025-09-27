from aiogram.filters import CommandStart, Command
from aiogram import Router, types
from aiogram.utils import markdown
from aiogram.enums import ParseMode

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://www.citypng.com/public/uploads/preview/hd-python-logo-symbol-transparent-png-735811696257415dbkifcuokn.png"
    await message.answer(
        text=f"{markdown.hide_link(url=url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
    )


@router.message(Command("help", prefix="/!%"))
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
