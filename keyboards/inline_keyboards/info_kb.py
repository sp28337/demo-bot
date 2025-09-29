from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def build_info_keyboard() -> InlineKeyboardMarkup:
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
    row_tg = [
        tg_channel_btn,
        tg_chat_btn,
    ]
    row_second = [bot_source_btn]
    # row_first = [tg_channel_btn]
    # row_second = [tg_chat_btn]
    rows = [
        # row_first,
        # row_second,
        row_tg,
        row_second,
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
