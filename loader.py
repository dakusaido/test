import src

from aiogram import Router, Dispatcher, Bot
from src.config import TELEGRAM_BOT_TOKEN

# All handlers should be attached to the Router (or Dispatcher)
router = Router()

# [Includes]
router.include_router(src.router)

# Dispatcher is a root router
dp = Dispatcher()

# ... and all other routers should be attached to Dispatcher
dp.include_router(router)

# Initialize Bot instance with a default parse mode which will be passed to all API calls
bot = Bot(TELEGRAM_BOT_TOKEN)
