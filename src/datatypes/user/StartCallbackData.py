from typing import Optional

from aiogram.filters.callback_data import CallbackData


class Start(CallbackData, prefix="start"):
    start: Optional[bool] = None
