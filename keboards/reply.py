from aiogram import types


def get_courses():
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=[
            [types.KeyboardButton(text='USD')],
            [types.KeyboardButton(text='EUR')]
        ],
        resize_keyboard=True
    )
    return keyboard