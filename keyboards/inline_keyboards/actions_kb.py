from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


random_num_updated_callback_data = "random_num_updated_callback_data"


def build_actions_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Rundom number",
        callback_data=random_num_updated_callback_data,
    )
    return builder.as_markup()
