from aiogram import types

from keyboards.default import areas
from loader import dp

# just in case the client made a mistake while picking the area
# we provide him with the opportunity to come back to the previous step
@dp.message_handler(text="Вернуться назад")
async def go_back(message: types.Message):
    await message.answer("Хорошо, давай попробуем заново", reply_markup=areas)
