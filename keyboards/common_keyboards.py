from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


class ButtonText:
    HELLO = "Hello!"
    WHATS_NEXT = "What's next?"
    BYE = "Bye-Bye!"


def get_on_start_keyboard() -> ReplyKeyboardMarkup:
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WHATS_NEXT)
    button_bye = KeyboardButton(text=ButtonText.BYE)
    buttons_first_row = [button_hello, button_help]
    buttons_second_row = [button_bye]
    markup = ReplyKeyboardMarkup(
        keyboard=[buttons_first_row, buttons_second_row],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    return markup


def get_on_help_keyboard() -> ReplyKeyboardMarkup:
    numbers = [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "0",
    ]
    buttons_row = [KeyboardButton(text=num) for num in numbers]
    # markup = ReplyKeyboardMarkup(
    #     keyboard=[buttons_row, buttons_row],
    #     resize_keyboard=True,
    # )
    # return markup

    builder = ReplyKeyboardBuilder()
    for num in numbers:
        # builder.add(KeyboardButton(text=num))
        #   or
        builder.button(text=num)
    # builder.adjust(3, 3, 4)
    builder.adjust(3)
    builder.row(buttons_row[3], buttons_row[1])
    return builder.as_markup(resize_keyboard=False)
