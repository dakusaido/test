from typing import Any, Optional

from aiogram.filters.callback_data import CallbackData


class Back(CallbackData, prefix="back"):
    method: str
    kwarg: Optional[Any] = None
    not_edit: Optional[bool] = None


class PrePage(CallbackData, prefix="pre_page"):
    pre_page: int
    method: str


class NextPage(CallbackData, prefix="next_page"):
    next_page: int
    method: str
