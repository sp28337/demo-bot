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


class ProductActions(IntEnum):
    details = auto()
    update = auto()
    delete = auto()


class ProductCallbackData(CallbackData, prefix="product"):
    actions: ProductActions
    id: int
    title: str
    price: int


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
    for index, (name, price) in enumerate(
        [
            ("Bread", 50),
            ("Tablet", 1450),
            ("Mobile", 4550),
        ],
        start=1,
    ):
        builder.button(
            text=name,
            callback_data=ProductCallbackData(
                actions=ProductActions.details,
                id=index,
                title=name,
                price=price,
            ),
        )
    builder.adjust(1)
    return builder.as_markup()


def build_products_details_keyboard(
    product_cb_data: ProductCallbackData,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text="Back to products",
        callback_data=ShopCallbackData(actions=ShopActions.products).pack(),
    )

    for label, action in [
        ("Update", ProductActions.update),
        ("Delete", ProductActions.delete),
    ]:
        builder.button(
            text=label,
            callback_data=ProductCallbackData(
                actions=action,
                # **product_cb_data.model_dump(exclude={"actions"})
                #      or
                **product_cb_data.model_dump(include={"id", "title", "price"}),
                #      or
                # id=product_cb_data.id,
                # title=product_cb_data.title,
                # price=product_cb_data.price,
            ).pack(),
        )
    builder.adjust(1, 2)
    return builder.as_markup()


def build_update_product_keyboard(
    product_cb_data: ProductCallbackData,
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(
        text=f"Back to {product_cb_data.title}",
        callback_data=ProductCallbackData(
            actions=ProductActions.details,
            **product_cb_data.model_dump(include={"id", "title", "price"}),
        ),
    )
    builder.button(
        text="Update",
        callback_data="...",
    )
    return builder.as_markup()
