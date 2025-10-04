from enum import IntEnum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ShopActions(IntEnum):
    products = auto()
    address = auto()
    root = auto()


class ShopCallbackData(CallbackData, prefix="shop"):
    actions: ShopActions


def build_shop_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Show products",
        callback_data=ShopCallbackData(actions=ShopActions.products).pack(),
    )
    builder.button(
        text="My address",
        callback_data=ShopCallbackData(actions=ShopActions.address).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()


def build_products_keyboard() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Back to root",
        callback_data=ShopCallbackData(actions=ShopActions.root).pack(),
    )
    builder.adjust(1)
    return builder.as_markup()
