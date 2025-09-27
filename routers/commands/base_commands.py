from aiogram.filters import CommandStart, Command
from aiogram import Router, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import markdown
from aiogram.enums import ParseMode

router = Router(name=__name__)


def get_on_start_keyboard():
    button_hello = KeyboardButton(text="Hello!")
    button_help = KeyboardButton(text="What's next?")
    buttons_first_row = [button_hello]
    buttons_second_row = [button_help]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_first_row, buttons_second_row])
    return markup


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://www.citypng.com/public/uploads/preview/hd-python-logo-symbol-transparent-png-735811696257415dbkifcuokn.png"
    await message.answer(
        text=f"{markdown.hide_link(url=url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
        reply_markup=get_on_start_keyboard(),
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
