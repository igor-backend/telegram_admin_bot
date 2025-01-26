import asyncio
import logging
from os import getenv

from handlers.info import info_router
from handlers.start import start_router

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode


TOKEN = getenv('BOT_TOKEN')


async def main() -> None:

    dispatcher = Dispatcher()
    dispatcher.include_routers(
        start_router,
        info_router,
    )

    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
