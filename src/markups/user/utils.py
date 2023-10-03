from typing import Dict, Union, Optional, Any

from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder

from src.datatypes.user import BackCallbackData

__all__ = ["get_markup", "get_back"]


def get_markup(
        dict_: Dict[str, Union[str, CallbackData]],
        *size: int
):
    builder = InlineKeyboardBuilder()

    for text, callback_data in dict_.items():
        builder.button(text=text, callback_data=callback_data)

    builder.adjust(*size)

    return builder.as_markup()


def get_back(method: str, kwarg: Optional[Any] = None, not_edit: Optional[bool] = None):
    builder = InlineKeyboardBuilder()
    builder.button(text="<-- Back", callback_data=BackCallbackData.Back(
        method=method,
        kwarg=kwarg,
        not_edit=not_edit
    ).pack())

    return builder.as_markup()