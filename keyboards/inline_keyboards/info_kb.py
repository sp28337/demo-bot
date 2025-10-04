from enum import Enum

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from .actions_kb import random_num_updated_callback_data


class RundomNumAction(Enum):
    dice = "dice"
    modal = "modal"


class RundomNumCallbackData(CallbackData, prefix="rundom_num"):
    action: RundomNumAction


def build_info_keyboard() -> InlineKeyboardMarkup:
    btn_random_cite = InlineKeyboardButton(
        text="Rundom number message",
        callback_data=random_num_updated_callback_data,
    )
    tg_channel_btn = InlineKeyboardButton(
        text="🔋 Канал",
        url="https://t.me/Khorenyan",
    )
    tg_chat_btn = InlineKeyboardButton(
        text="💬 Чат",
        url="https://t.me/SurenTalk",
    )
    bot_source_btn = InlineKeyboardButton(
        text="🤖 Исходный код",
        url="https://github.com/sp28337/demo-bot",
    )
    btn_random_num = InlineKeyboardButton(
        text="🎲 Случайное чсило",
        callback_data=RundomNumCallbackData(action=RundomNumAction.dice).pack(),
    )
    btn_random_modal = InlineKeyboardButton(
        text="🍆 Модальное окно",
        callback_data=RundomNumCallbackData(action=RundomNumAction.modal).pack(),
    )
    row_tg = [
        tg_channel_btn,
        tg_chat_btn,
    ]
    # row_first = [tg_channel_btn]
    # row_second = [tg_chat_btn]
    rows = [
        # row_first,
        # row_second,
        row_tg,
        [bot_source_btn],
        [btn_random_cite],
        [btn_random_num],
        [btn_random_modal],
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
