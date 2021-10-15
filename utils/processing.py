import time
from aiogram import types
from keyboards.default import areas
from keyboards.default import go_back
from loader import bot, db


# receiving an area name to offer the books that we have on the topic
async def prep(message: types.Message):
    await message.answer(text=f"Так, значит {message.text}. Я тебя понял. Тогда сейчас я пришлю тебе книги, "
                              f"которые помогут в изучении этого предмета", reply_markup=go_back)

# checking if there is more than a book from the list at our disposal, and if so, we offer it to the client
async def checking(list1, num: int, message: types.Message):
    for i in list1:
        id = i.payload
        amount = await db.how_much_in_possession(id)
        if int(amount) > 0:
            await bot.send_invoice(message.from_user.id, **i.generate_invoice())
            time.sleep(1)
            num += 1
    return num


# saying sorry for not having anything on the topic
async def sorry(message: types.Message):
    await message.answer(text=f"Извини, {message.from_user.first_name}... К сожалению все книги на эту тему раскупили.\n"
                              f"Но если хочешь, можешь попробовать выбрать что то на другую тему",
                         reply_markup=areas)

# main function controlling the processing
async def func(message: types.Message, var_list):
    num = 0
    await prep(message)
    time.sleep(2)
    num = await checking(var_list, num, message)
    if num == 0:
        await sorry(message)
