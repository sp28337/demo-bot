from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.utils import markdown

from .states import Survey

router = Router(name=__name__)


@router.message(Command("survey", prefix="!/%"))
async def handle_start_survey(
    message: types.Message,
    state: FSMContext,
):
    await state.set_state(Survey.full_name)
    await message.answer("Welcoe to our weekly survey! What's your name?")


@router.message(Survey.full_name, F.text)
async def handle_survey_user_full_name(
    message: types.Message,
    state: FSMContext,
):
    await state.update_data(full_name=message.text)
    await state.set_state(Survey.email)
    await message.answer(
        f"Hello, {markdown.hbold(message.text)}, now send me your email."
    )


@router.message(Survey.full_name)
async def handle_survey_user_full_name_invalid_content_type(
    message: types.Message,
):
    await message.answer(
        f"Sorry, I don't understand, send your name as text.",
    )


@router.message(Survey.email)
async def handle_survey_user_email(
    message: types.Message,
    state: FSMContext,
):
    await state.update_data(email=message.text)
    await state.set_state(Survey)
    await message.answer(text="Cool! ...")
