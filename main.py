import asyncio
import sys
import logging

from aiogram import Bot, Dispatcher
from config import Settings
from handlers import basic as basic_router


dp = Dispatcher()


async def main():
    bot = Bot(token=Settings.BOT_TOKEN)
    dp.include_router(basic_router.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
