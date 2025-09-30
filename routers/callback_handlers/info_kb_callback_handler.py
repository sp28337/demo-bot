from random import randint

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.info_kb import (
    random_num_dice_callback_data,
    random_num_modal_callback_data,
)

router = Router(name=__name__)


@router.callback_query(F.data == random_num_dice_callback_data)
async def handle_random_num_dice_cb(callback_query: CallbackQuery):
    await callback_query.answer(
        text=f"Your random dice is {randint(1, 6)}",
        cache_time=10,
    )


@router.callback_query(F.data == random_num_modal_callback_data)
async def handle_random_num_modal_cb(callback_query: CallbackQuery):
    await callback_query.answer(
        text=f"Your random num is {randint(1, 21)}",
        cache_time=5,
        show_alert=True,
    )
