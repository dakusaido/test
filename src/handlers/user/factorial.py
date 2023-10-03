import datetime
import sys

from aiogram.fsm.context import FSMContext

import src.markups as markup

from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, BufferedInputFile

from src.datatypes.user.FactorialCallbackData import Factorial
from src.datatypes.user import forms
from src.utils.factorial import Facto

router = Router()

sys.set_int_max_str_digits(0)


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
    try:
        number = int(message.text)

    except ValueError:
        await message.reply(
            text="The text you wrote is not a number.\nPlease write a NUMBER",
            reply_markup=markup.utils.get_back("getting_factorial_number")
        )
        return

    await message.answer(
        text="Calculating..."
    )

    facto = Facto()
    result = str(facto.calculate_factorial(number))

    if number > 1_000 or number < -1_000:
        result = result[:5]

    if len(result) > 5:
        time = datetime.datetime.utcnow().strftime("%Y-%m-%d_%H-%M-%S")
        filename = "factorial-" + time + ".txt"

        file = BufferedInputFile(
            file=str.encode(result),
            filename=filename
        )

        await message.reply_document(
            document=file,
            reply_markup=markup.utils.get_back("getting_factorial_number", not_edit=True)
        )

    else:
        await message.reply(
            text=result,
            reply_markup=markup.utils.get_back("getting_factorial_number", not_edit=True)
        )

    await state.clear()
