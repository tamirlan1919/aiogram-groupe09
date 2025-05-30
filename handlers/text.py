from aiogram import types, Router, F
from aiogram.types import Message
from aiogram.filters import Command


router = Router()

@router.message(F.text)
async def handle_text(message: Message):
    if message.text == 'C пюрешкой':
        await message.answer('Пюрешка с котлеткой')
    elif message.text == 'С макарошками':
        await message.answer('Макарошки с котлеткой')
    elif message.text == 'С рисом':
        await message.answer('Рис с котлеткой')
    else:
        await message.answer('Я не знаю такой порции, попробуй другую!')

