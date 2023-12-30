import logging
from aiogram import types
from aiogram.dispatcher.handler import CancelHandler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.utils.exceptions import ChatNotFound
from utils.misc import subscription
from loader import bot,db
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from data.config import ADMINS
from pprint import pprint
import sqlite3

class BigBrother(BaseMiddleware):

  async def on_pre_process_update(self, update: types.Update, data: dict):
    if update.message:
      user = update.message.from_user.id
      try:


        db.add_user(id=update.message.from_user.id,
                            name=update.message.from_user.full_name,)
        user_get = await bot.get_chat(update.message.from_user.id)
        user_bio = user_get.bio
        count = db.count_users()[0]
        await bot.send_message(chat_id='-1001903119428',
                                                   text=f"<b>🆕 Новый пользователь!</b>\n"
                                                        f"<b>Имя:</b> {update.message.from_user.get_mention()}\n"
                                                        f"<b>Имя пользователя:</b> @{update.message.from_user.username}\n"
                                                        f"<b>ИДЕНТИФИКАТОР:</b> <code>{update.message.from_user.id}</code>\n"
                                                        f"<b>БИО:</b> {user_bio}\n"
                                                        f"➖➖➖➖➖➖➖\n"
                                                        f"<b>Общий:</b> {count} ta")
      except sqlite3.IntegrityError as err:pass
      if update.message.text == "/start":
        return
    elif update.callback_query:
      user = update.callback_query.from_user.id
      if update.callback_query.data == "check_subs":
          await update.callback_query.message.delete()
    else:
      return


      
    with open("middlewares/banned_users.txt", "r") as file:
      ids = file.read()
      ids = ids.split("/")
    logging.info(user)
    with open("middlewares/bot_stop.txt", "r") as file:
      active_nonActive = file.read()
    if int(active_nonActive) == 0:

      if str(user) in ADMINS:
        pass
      else:
        try:
          await update.message.answer(
              "⚙️С ботом ведутся технические работы...")
        except:
          await update.callback_query.message.answer(
              "⚙️С ботом ведутся технические работы...")
        raise CancelHandler

    else:
      if str(user) in ids:
        await update.message.answer(
            "<b>Вы забанены ботом</b>❌\n\n\nЕсли это ошибка, обратитесь к администратору: @abdurahmondev",
            disable_web_page_preview=True)
        # print(ids)
        raise CancelHandler()

      else:
        # print(ids)
        pass
        try:
          result = "Подпишитесь на эти каналы, чтобы использовать бота:\n"
          final_status = True
          CHANNELS = []
          with open("data/channels.txt") as file:
            channels = file.read()
            list_channels = channels.split(",")
            for channel in list_channels:
              if channel != "":

                CHANNELS.append(f"@{channel}")
          buttons = InlineKeyboardMarkup(row_width=1)
          for channel in CHANNELS:
            status = await subscription.check(user_id=user, channel=channel)
            final_status *= status
            channel = await bot.get_chat(channel)
            if not status:
              invite_link = await channel.export_invite_link()
              # result += (f"👉 <a href = '{invite_link}'>{channel.title}</a>👈\n")
              buttons.add(
                  InlineKeyboardButton(text=f"👉{channel.title}👈",
                                       url=f"{invite_link}"))
          buttons.add(
              InlineKeyboardButton(text="✅ Подписался",
                                   callback_data="check_subs"))
          if not final_status:
            try:
              await update.message.answer(result, reply_markup=buttons)
            except:

              await update.callback_query.message.answer(result,
                                                         reply_markup=buttons)
            raise CancelHandler()
        except ChatNotFound:
          pass
