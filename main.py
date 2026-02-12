import asyncio
import logging

from pymysql import IntegrityError
from environs import Env
from aiogram.types import Message
from aiogram import Bot, Dispatcher
from aiogram.filters.command import CommandStart

from database import register_user


env = Env()
env.read_env()


bot = Bot(token=env.str("BOT_TOKEN"))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message:Message):
    telegram_id = message.from_user.id
    fullname = message.from_user.full_name


    try:
        register_user(telegram_id=telegram_id, fullname=fullname)
        await message.answer(text="Assalomu alaykum, muvaffaqiyatli ro'yxatga olindingiz!")
    except IntegrityError:
        await message.answer(text="Qaytganingizdan xursandmiz !")


async def notify_admins():
    admins = env.list("ADMINS")

    for admin in admins:
        try:
            await bot.send_message(chat_id=admin, text="🤖 Botga yangilanish kiritildi !")
        except:
            pass

async def main():
    logging.basicConfig(level=logging.INFO)
    await notify_admins()
    await dp.start_polling(bot)


asyncio.run(main())