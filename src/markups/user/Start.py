from src.datatypes.user import StartCallbackData, FactorialCallbackData
from src.markups.user.utils import get_markup


class Start:

    def __init__(self):
        pass

    @staticmethod
    def get_start():
        dict_ = {
            "Calculate the factorial": FactorialCallbackData.Factorial(start=True).pack(),
            "🗨 New Dialog": StartCallbackData.Start(start=True).pack()
        }
        return get_markup(dict_, 1)

