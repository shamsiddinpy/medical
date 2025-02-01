import asyncio
import sys
from asyncio.log import logger
from pathlib import Path

from aiogram import Dispatcher, Bot
from aiogram.fsm.storage.memory import MemoryStorage

BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "root.settings")  # Loyiha nomini o'rnating
django.setup()
from root.settings import BOT_TOKEN

bot = Bot(token=BOT_TOKEN, )
storage = MemoryStorage()


async def main():
    dp = Dispatcher(storage=storage)
    from apps.bot import private_handler_router
    dp.include_router(private_handler_router)
    logger.info("Bot polling orqali ishga tushmoqda...")
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
