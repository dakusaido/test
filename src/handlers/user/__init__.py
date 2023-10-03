from aiogram import Router

from src.handlers.user import start, factorial

router = Router()

router.include_router(start.router)
router.include_router(factorial.router)
