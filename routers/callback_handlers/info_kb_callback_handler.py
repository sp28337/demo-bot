from random import randint

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.info_kb import (
    random_cite_callback_data,
    random_num_dice_callback_data,
)

router = Router(name=__name__)


@router.callback_query(F.data == random_cite_callback_data)
async def handle_random_cite_cb(callback_query: CallbackQuery):
    bot_me = await callback_query.bot.me()
    await callback_query.answer(
        url=f"t.me/{bot_me.username}?start={randint(1, 100)}",
    )


@router.callback_query(F.data == random_num_dice_callback_data)
async def handle_random_num_dice_cb(callback_query: CallbackQuery):
    await callback_query.answer(
        text=f"Your random dice is {randint(1, 6)}",
        cache_time=10,
    )
