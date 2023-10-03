from aiogram import Router

import src.handlers as handlers


router = Router()

router.include_router(handlers.router)
