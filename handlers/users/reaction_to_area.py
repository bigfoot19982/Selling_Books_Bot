import time

from aiogram import types
from aiogram.types import ContentType

from data import arab_list
from data import history_list
from data import the_world_list
from data import POST_REGULAR_SHIPPING, POST_FAST_SHIPPING, PICKUP_SHIPPING
from loader import dp, db
from utils.processing import func


# in the three following functions we catch the area of the client's interests and launch a processing function
@dp.message_handler(text="Арабский язык")
async def show_arab(message: types.Message):
    await func(message, arab_list)


@dp.message_handler(text="История")
async def show_history(message: types.Message):
    await func(message, history_list)


@dp.message_handler(text="Окружающий мир")
async def show_the_world(message: types.Message):
    await func(message, the_world_list)


# sending shipping options if the client is from Russia (saying sorry otherwise)
@dp.shipping_query_handler()
async def shipping_q(query: types.ShippingQuery):
    if query.shipping_address.country_code == "RU":
        await dp.bot.answer_shipping_query(shipping_query_id=query.id, shipping_options=[
            POST_REGULAR_SHIPPING,
            POST_FAST_SHIPPING,
            PICKUP_SHIPPING
        ], ok=True)
    else:
        await dp.bot.answer_shipping_query(shipping_query_id=query.id, ok=False,
                                           error_message="Sorry, no shipping to your country")


@dp.pre_checkout_query_handler()
async def pre_checkout(query: types.PreCheckoutQuery):
    await dp.bot.answer_pre_checkout_query(pre_checkout_query_id=query.id, ok=True)
    time.sleep(1)
    await dp.bot.send_message(chat_id=query.from_user.id, text="Спасибо за покупку!\nОжидайте доставку!")


# on receipt of successful payment we add the order into the DB,
# decrease "units_in_stock" value of the book and send a notification for all admins about a new order
@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def finish_of_payment(message: types.Message):
    await db.add_order(message)
    await db.minus_unit(message.successful_payment.invoice_payload)
    await db.notify_admin(dp)
