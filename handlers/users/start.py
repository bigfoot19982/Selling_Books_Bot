from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default.areas import areas
from loader import dp

# greeting
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(
        f"Привет, {message.from_user.full_name}! Вижу, тебе интересны мои книги. Давай выберем область, которая тебе нравится",
        reply_markup=areas)
