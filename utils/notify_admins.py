import logging

from aiogram import Dispatcher

from data.config import ADMINS

# notification for admins that the bot is launched
async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
