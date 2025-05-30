from aiogram import types, Router
from aiogram.types import Message
from aiogram.filters import Command



router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    kb = [
        [types.KeyboardButton(text='Погода'), types.KeyboardButton(text='Новости')],
        [types.KeyboardButton(text='Курс валют')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
    await message.answer('Выберите опцию:',
                         reply_markup=keyboard)


@router.message(Command("help"))
async def cmd_help(message: Message):
    kb = [
        [types.KeyboardButton(text='Отправить геолокацию', request_location=True),
          types.KeyboardButton(text='Отправить контакт', request_contact=True)],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                          input_field_placeholder='Выбери действие')
    await message.answer('Я могу отправить тебе геолокацию или контакт',
                         reply_markup=keyboard)


@router.message(Command('menu'))
async def cmd_menu(message: Message):
    kb = [
        [types.InlineKeyboardButton(text='Пюрешка с котлеткой', callback_data='p1')],
        [types.InlineKeyboardButton(text='Макарошки с котлеткой', callback_data='p2')],
        [types.InlineKeyboardButton(text='Рис с котлеткой', callback_data='p3')],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=kb)
    await message.answer('Выбери порцию котлеты',
                         reply_markup=keyboard)
    