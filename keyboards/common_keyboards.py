from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButtonPollType,
)
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


def get_actions_keyboard() -> ReplyKeyboardMarkup:
    # markup = ReplyKeyboardMarkup(
    #     keyboard=[],
    # )
    # return markup
    #
    #     or
    builder = ReplyKeyboardBuilder()

    # builder.add(KeyboardButton(text="Send location", request_location=True))
    #     or
    builder.button(text="🌎 Send Location", request_location=True)
    builder.button(text="☎️ Send My Phone", request_contact=True)
    builder.button(text="☎📊 Send Poll", request_poll=KeyboardButtonPollType())
    builder.button(
        text="👾 Send Quiz", request_poll=KeyboardButtonPollType(type="quiz")
    )
    builder.button(
        text="🍽 Dinner?", request_poll=KeyboardButtonPollType(type="regular")
    )
    builder.button(text=ButtonText.BYE)
    builder.adjust(1)

    return builder.as_markup(
        input_field_placeholder="Actions:",
        resize_keyboard=True,
    )


def build_yes_or_no_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.button(text="yes")
    builder.button(text="no")
    # builder.adjust(1)
    return builder.as_markup(resize_keyboard=True)
