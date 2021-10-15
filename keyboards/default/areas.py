from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

areas = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Арабский язык")
        ],
        [
            KeyboardButton(text="История")
        ],
        [
            KeyboardButton(text="Окружающий мир")
        ],
    ],
    resize_keyboard=True
)
