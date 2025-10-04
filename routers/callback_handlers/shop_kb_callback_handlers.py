from aiogram import Router, F
from aiogram.types import CallbackQuery

from keyboards.inline_keyboards.shop_kb import (
    ShopActions,
    ShopCallbackData,
    build_shop_keyboard,
    build_products_keyboard,
)

router = Router(name=__name__)


@router.callback_query(
    ShopCallbackData.filter(F.actions == ShopActions.products),
)
async def send_products_list(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Available products:",
        reply_markup=build_products_keyboard(),
    )


@router.callback_query(
    ShopCallbackData.filter(F.actions == ShopActions.root),
)
async def handle_my_root_button(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text(
        text="Your shop actions:",
        reply_markup=build_shop_keyboard(),
    )


@router.callback_query(
    ShopCallbackData.filter(F.actions == ShopActions.address),
)
async def handle_my_address_button(call: CallbackQuery):
    await call.answer(
        text="Your address section is steel in progress...",
        cache_time=30,
    )
