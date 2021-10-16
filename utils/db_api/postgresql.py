import asyncio
from datetime import datetime

import asyncpg
import logging
from aiogram import types, Dispatcher
from aiogram.utils.markdown import hcode

from data import config
from data.config import ADMINS
from utils.db_api.big_scripts import create_tab_books, create_tab_orders, notify_adms, how_much, add_ord


class Database:
    #connecting the DB
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
        sql = create_tab_books
        await self.pool.execute(sql)

    async def create_table_orders(self):
        sql = create_tab_orders
        await self.pool.execute(sql)

    async def add_order(self, message: types.Message):
        sql = add_ord

        book_id = int(message.successful_payment.invoice_payload)
        buyer_name = message.successful_payment.order_info.name
        phone = message.successful_payment.order_info.phone_number
        shipping_address = await Database.form_address(message)
        total_amount = message.successful_payment.total_amount
        shipping_option = message.successful_payment.shipping_option_id
        order_date = datetime.now()
        done = False

        await self.pool.execute(sql, book_id, buyer_name, phone, shipping_address,
                                total_amount, shipping_option, order_date, done)

    async def how_much_in_possession(self, id: str):
        int_id = int(id)
        sql = how_much
        return await self.pool.fetchval(sql, int_id)

    # decrementing "units_in_stock" of a particular book in the DB
    async def minus_unit(self, id: str):
        new_id = int(id)
        sql = "SELECT COUNT (units_in_stock) FROM books WHERE book_id = $1"
        num = await self.pool.fetchval(sql, new_id)
        num -= 1
        new_sql = "UPDATE books SET units_in_stock = $1 WHERE book_id = $2"
        await self.pool.execute(new_sql, num, new_id)

    # picking up the id of the last emerged order
    async def prev(self):
        sql = "SELECT MAX(order_id) FROM orders"
        return await self.pool.fetchval(sql)

    # notification for admins of a new order
    async def notify_admin(self, dp: Dispatcher):
        sql = notify_adms
        val = await self.prev()
        data = await self.pool.fetchrow(sql, val)

        for admin in ADMINS:
            try:
                await dp.bot.send_message(admin,
                                          text=hcode(
                                              "{buyer_name} хочет приобрести книгу {book_name}({shipping_option}). \nПроверьте базу данных. order_id = {order_id}".format(
                                                  **data)))

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
