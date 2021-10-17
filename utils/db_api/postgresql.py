import asyncio
from datetime import datetime

import asyncpg
import logging
from aiogram import types, Dispatcher
from aiogram.utils.markdown import hcode

from data import config
from data.config import ADMINS
from utils.db_api.big_scripts import create_tab_books, create_tab_orders, how_much, add_ord, \
    get_ship_address, count_units_in_stock, update_units_in_stock, last_order, order_data, ask_ship_opt
from utils.db_api.constants_for_shipping_address import get_constants


class Database:
    # connecting the DB
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                user=config.PGUSER,
                password=config.PGPASSWORD,
                host=config.IP, max_inactive_connection_lifetime=3
            )
        )

    # a method to convert ShippingAddress type into str
    @staticmethod
    async def form_address(message: types.Message):
        shipping_address = ""
        tmp_address = message.successful_payment.order_info.shipping_address
        last_elem = tmp_address.post_code
        for subst in tmp_address:
            shipping_address += str(subst)
            if subst != last_elem:
                shipping_address += ' '
        return shipping_address

    async def create_table_books(self):
        await self.pool.execute(create_tab_books)

    async def create_table_orders(self):
        await self.pool.execute(create_tab_orders)

    async def add_order(self, message: types.Message):
        book_id = int(message.successful_payment.invoice_payload)
        buyer_name = message.successful_payment.order_info.name
        phone = message.successful_payment.order_info.phone_number
        shipping_address = await Database.form_address(message)
        total_amount = message.successful_payment.total_amount
        shipping_option = message.successful_payment.shipping_option_id
        order_date = datetime.now()
        done = False

        await self.pool.execute(add_ord, book_id, buyer_name, phone, shipping_address, total_amount, shipping_option,
                                order_date, done)

    async def how_much_in_possession(self, id: str):
        return await self.pool.fetchval(how_much, int(id))

    # decrementing "units_in_stock" of a particular book in the DB
    async def minus_unit(self, id: str):
        num = await self.pool.fetchval(count_units_in_stock, int(id))
        num -= 1
        await self.pool.execute(update_units_in_stock, num, int(id))

    # picking up the id of the last emerged order
    async def prev(self):
        return await self.pool.fetchval(last_order)

    async def shipping_option(self):
        prev_ord = await self.prev()
        ship_opt = await self.pool.fetchval(ask_ship_opt, prev_ord)
        shipping_answer = "заберет заказ сам" if ship_opt == "pick_up" else "хочет получить товар быстро, VIP доставкой" if ship_opt == "vip_sh" else " выбрал обычную доставку"
        return shipping_answer

    # notification for admins of a new order
    async def notify_admin(self, dp: Dispatcher):
        prev_ord = await self.prev()
        data = await self.pool.fetchrow(order_data, prev_ord)
        ship_address = await self.pool.fetchval(get_ship_address, prev_ord)
        constants = await get_constants(ship_address)

        for admin in ADMINS:
            try:
                await dp.bot.send_message(admin,
                                          text=f"Поступил заказ из города {ship_address[constants[0]:constants[1]]}, улица {ship_address[constants[2]:constants[3]]}, индекс {ship_address[constants[4]:constants[5]]}.\n\n" + hcode(
                                              "{buyer_name} хочет приобрести книгу {book_name}. \nПроверьте базу данных: order_id = {order_id}.".format(
                                                  **data)) + f"\n\nКлиент {await self.shipping_option()}.")

            except Exception as err:
                logging.exception(err)

    # switching the value of "done" column into true, which signifies that the order is carried out
    async def implemented(self, message: types.Message):
        order_id = int("".join(filter(str.isdigit, message.reply_to_message.text)))
        sql = "UPDATE orders SET done = True WHERE order_id = $1"
        await self.pool.execute(sql, order_id)

    # counting the number of non implemented orders
    async def count(self):
        sql = "SELECT COUNT(*) FROM orders WHERE done = false"
        return await self.pool.fetchval(sql)
