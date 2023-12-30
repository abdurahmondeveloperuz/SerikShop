import sqlite3

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.buttons import buttons
from time import sleep
from data.config import ADMINS
from loader import dp, db, bot,balance

from aiogram.dispatcher import FSMContext
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message,state:FSMContext):
    name = message.from_user.full_name
    user_id = message.from_user.id

    # Foydalanuvchini bazaga qo'shamiz
    user_balance = balance.get_balance(user_id=user_id)
    await message.answer(
f"""
📛Ваше имя: <i>{name}</i>
💰Ваш баланс: {user_balance} ₽

🆔Идентификационный номер: <code>{user_id}</code>"""
,reply_markup=buttons)

