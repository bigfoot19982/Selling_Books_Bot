from aiogram import executor

from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # creating table books
    print("Создаем таблицу книг")
    try:
        await db.create_table_books()
    except Exception as err:
        print(err)

    # creating table orders
    print("Создаем таблицу ордеров")
    try:
        await db.create_table_orders()
    except Exception as error:
        print(error)

    await set_default_commands(dispatcher)

    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
