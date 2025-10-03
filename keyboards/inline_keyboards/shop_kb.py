from enum import Enum, auto

from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


class ShopActions(Enum):
    products = auto()
    address = auto()


class ShopCallbackData(CallbackData, prefix="shop"):
    actions: ShopActions


def build_shop_keyboarb() -> InlineKeyboardMarkup:
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
