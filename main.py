from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN
import logging
from database.models import create_table_users
from database.crud import add_user, get_user
from aiogram.client.default import DefaultBotProperties
import datetime

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode='HTML'))
dp = Dispatcher()



@dp.message(Command("start"))
async def cmd_start(message: Message):
    user = get_user(message.from_user.id)
    if user is not None:
        await message.answer("<b>Привет</b>, Ты уже зарегистрирован в базе данных.")
    else:
        today = datetime.datetime.now()
        add_user(username=message.from_user.username, 
                telegram_id =message.from_user.id,
                created_at=str(today))
        
        await message.answer("Привет <b>я бот</b>, который умеет работать с командами.")

@dp.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Ты можешь связаться со мной через <a href = 'https://google.com/'>это</a>")

@dp.message(F.text)
async def cmd_text(message: Message):
    if message.text.lower() == 'привет':
        await message.answer('Привет брат)')

    elif message.text.lower() == 'как дела?':
        await message.answer('Нормально, а у тебя?')

    elif message.text.lower() == 'что ты умеешь?':
        await message.answer('Я умею отвечать на команды и текстовые сообщения.')

    else:
        await message.answer('Я не знаю такой команды, напиши /help')


async def main():
    logging.basicConfig(level=logging.INFO)
    create_table_users()
    await dp.start_polling(bot)

if __name__ == '__main__': 
    import asyncio
    asyncio.run(main())