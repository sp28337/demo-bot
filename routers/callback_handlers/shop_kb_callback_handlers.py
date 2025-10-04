from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.utils import markdown

from keyboards.inline_keyboards.shop_kb import (
    ShopActions,
    ShopCallbackData,
    ProductActions,
    ProductCallbackData,
    build_shop_keyboard,
    build_products_keyboard,
    build_products_details_keyboard,
    build_update_product_keyboard,
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


@router.callback_query(
    ProductCallbackData.filter(F.actions == ProductActions.details),
)
async def handle_my_product_detail_button(
    call: CallbackQuery,
    callback_data: ProductCallbackData,
):
    await call.answer()
    message_text = markdown.text(
        markdown.hbold(f"Product #{callback_data.id}"),
        markdown.text(
            markdown.hbold("Title:"),
            callback_data.title,
        ),
        markdown.text(
            markdown.hbold("Price:"),
            callback_data.price,
        ),
        sep="\n",
    )
    await call.message.edit_text(
        text=message_text,
        reply_markup=build_products_details_keyboard(callback_data),
    )


@router.callback_query(
    ProductCallbackData.filter(F.actions == ProductActions.delete),
)
async def handle_my_product_delete_button(call: CallbackQuery):
    await call.answer(
        text="Delete is steel in progress...",
    )


@router.callback_query(
    ProductCallbackData.filter(F.actions == ProductActions.update),
)
async def handle_my_product_update_button(
    call: CallbackQuery,
    callback_data: ProductCallbackData,
):
    await call.answer()
    await call.message.edit_reply_markup(
        reply_markup=build_update_product_keyboard(callback_data)
    )
