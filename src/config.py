from os import getenv

from dotenv import load_dotenv

load_dotenv()

# Bot token can be obtained via https://t.me/BotFather
TELEGRAM_BOT_TOKEN = getenv('TELEGRAM_BOT_TOKEN')
