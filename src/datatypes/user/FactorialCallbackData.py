from typing import Optional

from aiogram.filters.callback_data import CallbackData


class Factorial(CallbackData, prefix="factorial"):
    start: Optional[bool] = None
