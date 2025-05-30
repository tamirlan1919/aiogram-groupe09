from aiogram import types, Router, F
from aiogram.types import Message
from aiogram.filters import Command
from keboards.reply import get_courses

router = Router()

@router.message(F.text)
async def handle_text(message: Message):
    if message.text == 'Курс валют':
        keyboard = get_courses()
        await message.answer('Выбери валюту', reply_markup=keyboard)
    elif message.text == 'С макарошками':
        await message.answer('Макарошки с котлеткой')
    elif message.text == 'С рисом':
        await message.answer('Рис с котлеткой')
    else:
        await message.answer('Я не знаю такой порции, попробуй другую!')

