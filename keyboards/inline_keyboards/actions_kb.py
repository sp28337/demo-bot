from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


random_num_updated_callback_data = "random_num_updated_callback_data"


def build_actions_keyboard() -> InlineKeyboardMarkup:
    btn_random_cite = InlineKeyboardButton(
        text="Rundom number message",
        callback_data=random_num_updated_callback_data,
    )
    rows = [
        [btn_random_cite],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
