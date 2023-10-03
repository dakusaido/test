import asyncio
import logging
import os

from typing import NoReturn

from dotenv import load_dotenv

from app import dp, bot


async def main() -> NoReturn:
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    load_dotenv()

    if os.getenv("DEBUG") == "1":
        logging.basicConfig(level=logging.INFO)

    asyncio.run(main())
