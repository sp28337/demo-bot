from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


random_cite_callback_data = "random_cite_callback_data"  # from 1 to 64 bytes


def build_info_keyboard() -> InlineKeyboardMarkup:
    btn_random_cite = InlineKeyboardButton(
        text="Random cite",
        callback_data=random_cite_callback_data,
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
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup
