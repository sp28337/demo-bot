from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ButtonText:
    HELLO = "Hello!"
    WHATS_NEXT = "What's next?"
    BYE = "Bye-Bye!"


def get_on_start_keyboard():
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
