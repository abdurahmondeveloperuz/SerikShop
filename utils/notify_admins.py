import logging
from aiogram import Dispatcher


async def on_startup_notify(dp: Dispatcher):
    await dp.bot.send_message(chat_id='-1001903119428',text="✅Бот запущен")

async def on_shutdown_notify(dp: Dispatcher):
   await dp.bot.send_message(chat_id='-1001903119428', text="❌Бот выключен")
