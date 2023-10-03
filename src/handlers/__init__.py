from aiogram import Router

import src.handlers.user as user

router = Router()

router.include_router(user.router)