from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


random_num_updated_callback_data = "random_num_updated_callback_data"


def build_actions_keyboard(text="Rundom number") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=text,
        callback_data=random_num_updated_callback_data,
    )
    return builder.as_markup()
