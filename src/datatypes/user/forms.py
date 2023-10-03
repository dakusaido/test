from aiogram.fsm.state import StatesGroup, State


class CalculatingFactorial(StatesGroup):
    start = State()
