from aiogram.fsm.context import FSMContext

import src.markups as markup

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery

from src.datatypes.user import StartCallbackData
from src.datatypes.user.BackCallbackData import Back

router = Router()


@router.message(Command(commands=["start", "new_dialog"]))
async def command_start_handler(message: Message) -> None:
    text = "🧐 Choose what information do you want to know?"
    await message.answer(text, reply_markup=markup.Start.get_start())


@router.callback_query(StartCallbackData.Start.filter(F.start))
async def go_to_start(query: CallbackQuery, state: FSMContext):
    await query.answer()
    await state.clear()
    await command_start_handler(query.message)


@router.callback_query(Back.filter(F.method == "start"))
async def back_to_start(query: CallbackQuery, state: FSMContext):
    await query.answer()
    await state.clear()
    text = "🧐 Choose what information do you want to know?"
    await query.message.edit_text(text, reply_markup=markup.Start.get_start())


@router.callback_query(Back.filter(F.method == "getting_factorial_number"))
async def back_to_getting_user_methods(query: CallbackQuery, callback_data: Back, state: FSMContext):
    await back_to_start(query, state)
