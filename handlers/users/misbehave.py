from aiogram import types

from loader import dp

# calling on the client to keep to the pattern
@dp.message_handler(state=None)
async def misbehave(message: types.Message):
    await message.answer(f"Дорогой {message.from_user.first_name}! Не пиши ерунду, пожалуйста. Следуй инструкции.")
