from random import randint

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


random_num_updated_callback_data = "random_num_updated_callback_data"


class FixedRandomNumCallbackData(CallbackData, prefix="fixed-random-num"):
    number: int


def build_actions_keyboard(text="Rundom number") -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=text,
        callback_data=random_num_updated_callback_data,
    )
    callback_data_1 = FixedRandomNumCallbackData(number=randint(1, 100))
    builder.button(
        text=f"Rundom number: {callback_data_1.number}",
        callback_data=callback_data_1.pack(),
    )
    builder.button(
        text="Rundom number: [HIDDEN]",
        callback_data=FixedRandomNumCallbackData(number=randint(1, 100)).pack(),
    )
    builder.adjust(1)  # одна колонка
    return builder.as_markup()
