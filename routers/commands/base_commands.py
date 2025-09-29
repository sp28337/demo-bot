from aiogram.filters import CommandStart, Command
from aiogram import Router, types, F
from aiogram.utils import markdown
from aiogram.enums import ParseMode

from keyboards.common_keyboards import (
    ButtonText,
    get_on_start_keyboard,
    get_on_help_keyboard,
    get_actions_keyboard,
)
from keyboards.inline_keyboards.info_kb import build_info_keyboard

router = Router(name=__name__)


@router.message(CommandStart())
async def handle_start(message: types.Message):
    url = "https://www.citypng.com/public/uploads/preview/hd-python-logo-symbol-transparent-png-735811696257415dbkifcuokn.png"
    print("Command text:", repr(message.text))
    await message.answer(
        text=f"{markdown.hide_link(url=url)}Hello, {markdown.hbold(message.from_user.full_name)}!",
        parse_mode=ParseMode.HTML,
        reply_markup=get_on_start_keyboard(),
    )


@router.message(F.text == ButtonText.WHATS_NEXT)
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
    await message.answer(
        text=text,
        parse_mode=ParseMode.MARKDOWN_V2,
        reply_markup=get_on_help_keyboard(),
    )


@router.message(Command("more", prefix="/!%"))
async def handle_more(message: types.Message):
    markup = get_actions_keyboard()
    await message.answer(
        text="Choose action:",
        reply_markup=markup,
    )


@router.message(Command("info", prefix="/!%"))
async def handle_info(message: types.Message):
    markup = build_info_keyboard()
    await message.answer(
        text="Ссылки и прочие ресурсы:",
        reply_markup=markup,
    )
