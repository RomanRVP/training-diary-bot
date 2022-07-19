import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher
from aiogram.dispatcher.fsm.storage.memory import MemoryStorage

from config import BOT_TOKEN


logging.basicConfig(level=logging.INFO)


async def main():

    dp = Dispatcher()
    # dp.include_router( роутер майбутнього хендлеру )

    bot = Bot(token=BOT_TOKEN)
    await dp.start_polling(bot, storage=MemoryStorage)


if __name__ == '__main__':
    asyncio.run(main())
