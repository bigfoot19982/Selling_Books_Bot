from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

go_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Вернуться назад")
        ],
    ],
    resize_keyboard=True
)
