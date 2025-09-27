from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


class ButtonText:
    HELLO = "Hello!"
    WHATS_NEXT = "What's next?"


def get_on_start_keyboard():
    button_hello = KeyboardButton(text=ButtonText.HELLO)
    button_help = KeyboardButton(text=ButtonText.WHATS_NEXT)
    buttons_first_row = [button_hello]
    buttons_second_row = [button_help]
    markup = ReplyKeyboardMarkup(keyboard=[buttons_first_row, buttons_second_row])
    return markup
