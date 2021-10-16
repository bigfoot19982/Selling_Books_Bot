from aiogram import types

from data.config import ADMINS
from loader import db, dp


# checking if the message is from one of the admins
async def is_from_admin(message: types.Message):
    id = int(message.from_user.id)
    for admin in ADMINS:
        if id == int(admin):
            return True
    return False


# when one of the admins carried out the order he sends
# key word "Исполнено" to the bot to switch "done" value of the order into true
@dp.message_handler(text="Исполнено")
async def implemented_order(message: types.Message):
    if await is_from_admin(message):
        await db.implemented(message)


# a way for admin to know how many orders he is to attend to
@dp.message_handler(text="Сколько невыполненных заказов?")
async def pending_orders(message: types.Message):
    if await is_from_admin(message) == True:
        num = await db.count()
        await dp.bot.send_message(message.from_user.id, text=f"Количество невыполненных заказов в базе: {num}.")
