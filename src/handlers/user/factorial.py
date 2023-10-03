from aiogram.fsm.context import FSMContext

import src.markups as markup

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery

from src.datatypes.user.FactorialCallbackData import Factorial
from src.datatypes.user import forms
from src.utils.factorial import get_factorial

router = Router()


@router.callback_query(Factorial.filter(F.start))
async def start_to_facto(
        query: CallbackQuery,
        callback_data: Factorial,
        state: FSMContext
):
    await query.answer()
    await state.set_state(forms.CalculatingFactorial.start)

    text = "Please write a number"

    # if query:
    await query.message.answer(
        text=text,
        reply_markup=markup.utils.get_back("getting_factorial_number"),
        parse_mode="HTML"
    )


@router.message(forms.CalculatingFactorial.start)
async def final_facto(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply(
            text="The text you wrote is not a number.\nPlease write a NUMBER",
            reply_markup=markup.utils.get_back("getting_factorial_number")
        )
        return

    await message.answer(
        text="Calculating..."
    )

    number = int(message.text)

    facto = get_factorial(number)

    await message.reply(
        text=str(facto)
    )
    await state.clear()
