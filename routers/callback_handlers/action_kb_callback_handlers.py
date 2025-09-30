from random import randint

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.actions_kb import build_actions_keyboard
from keyboards.inline_keyboards.info_kb import (
    random_num_updated_callback_data,
)

router = Router(name=__name__)


@router.callback_query(F.data == random_num_updated_callback_data)
async def handle_random_number_edited(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=f"Random number: {randint(1, 100)}",
        reply_markup=build_actions_keyboard(text="Generate again"),
    )
