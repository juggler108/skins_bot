from aiogram import Bot, Dispatcher
from aiogram.types import Message, ContentType
from core.handlers.basic import get_start, get_faq, get_our_location, get_main_menu, get_consultation, get_our_social, \
    get_about_us
import asyncio
import logging
from core.settings import settings
from aiogram.filters import Command, Text
from aiogram import F
from core.utils.commands import set_commands
from datetime import datetime, timedelta


async def start_bot(bot: Bot):
    await set_commands(bot)
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(chat_id=settings.bots.admin_id, text='Бот остановлен!')


async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s")

    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')
    dp = Dispatcher()

    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)

    # dp.message.register(get_inline, Command(commands='inline'))
    # dp.message.register(get_hello, F.text.lower() == 'привет')
    dp.callback_query.register(get_about_us, Text(text='about'))
    dp.callback_query.register(get_our_social, Text(text='social'))
    dp.callback_query.register(get_consultation, Text(text='consultation'))
    dp.callback_query.register(get_main_menu, Text(text='main_menu'))
    dp.callback_query.register(get_our_location, Text(text='how_find_us'))
    dp.callback_query.register(get_faq, Text(text='faq'))
    dp.message.register(get_start, Command(commands=['start', 'run']))
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())
