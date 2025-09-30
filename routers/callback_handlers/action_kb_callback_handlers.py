from random import randint

from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.actions_kb import (
    build_actions_keyboard,
    random_num_updated_callback_data,
    FixedRandomNumCallbackData,
)

router = Router(name=__name__)


@router.callback_query(F.data == random_num_updated_callback_data)
async def handle_random_number_edited(callback_query: CallbackQuery):
    await callback_query.answer()
    await callback_query.message.edit_text(
        text=f"Random number: {randint(1, 100)}",
        reply_markup=build_actions_keyboard(text="Generate again"),
    )


@router.callback_query(FixedRandomNumCallbackData.filter())
async def handle_fixed_random_number_callback(
    callback_query: CallbackQuery,
    callback_data: FixedRandomNumCallbackData,
):
    await callback_query.answer(
        text=(
            f"You fixed random number is {callback_data.number}\n"
            f"Callback data: {callback_query.data!r}\n"
        ),
        show_alert=True,
    )
