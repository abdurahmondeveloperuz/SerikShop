import logging
from aiogram.types import CallbackQuery,Message,ParseMode
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from keyboards.default.buttons import buttons,panel_tugma,tugmasi,tugmasi_rek,tugmasi_user,channel_tools,ban_tools,ortga_to_panel,admin_tugma,ortga_to_main,bot_on_off,numbers_list_one,numbers_list_two,numbers_list_one_admin,numbers_list_two_admin
from datetime import datetime
from loader import dp,db,bot,balance
from data.config import ADMINS,fivesimnettoken as token
import pytz
from utils.api import get_balance
from time import sleep
import datetime as dt

@dp.callback_query_handler(text="buy_number")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("♦️ Нажмите нужную кнопку!",reply_markup=numbers_list_one)
@dp.callback_query_handler(text="buy_number")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("♦️ Нажмите нужную кнопку!",reply_markup=numbers_list_one)
@dp.callback_query_handler(text="next")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔜 Перенесено на следующую страницу!",reply_markup=numbers_list_two)
@dp.callback_query_handler(text="previus")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся на предыдущую страницу!",reply_markup=numbers_list_one)

@dp.callback_query_handler(text="next_edit")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔜 Перенесено на следующую страницу!",reply_markup=numbers_list_two_admin)
@dp.callback_query_handler(text="previus_edit")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся на предыдущую страницу!",reply_markup=numbers_list_one_admin)
@dp.callback_query_handler(state="*",text="ortga_to_main")
async def stats_users(call:types.CallbackQuery,state:FSMContext):
    await state.finish()
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=buttons)
@dp.callback_query_handler(text="ortga_to_main")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=buttons)
@dp.callback_query_handler(state='*',text="ortga_panel")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await state.finish()
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Хорошo вернулся",reply_markup=panel_tugma)
@dp.callback_query_handler(text="ortga_panel")
async def send_ad_to_all(call: types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Хорошo вернулся",reply_markup=panel_tugma)
@dp.callback_query_handler(text="ortga_to_social_one_admin")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=numbers_list_one_admin)
@dp.callback_query_handler(text="ortga_to_social_two_admin")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=numbers_list_two_admin)
@dp.callback_query_handler(text="ortga_to_social_one")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=numbers_list_one)
@dp.callback_query_handler(text="ortga_to_social_two")
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🔙 Вернулся",reply_markup=numbers_list_two)
@dp.callback_query_handler(text="balance")
async def bot_stat(call: types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    bot_start_date = dt.date(2023, 8, 25)
    farq = dt.date.today() - bot_start_date
    user_balance = balance.get_balance(user_id=call.from_user.id)
    await call.message.answer(f"""
<b>📛 Ваше имя:</b> <i>{call.message.chat.first_name}</i>
<b>✊ Ваше имя пользователя:</b> @{call.message.chat.username}
<b>🆔 Ваш идентификатор:</b> <code>{call.message.chat.id}</code>
<b>💰 Ваш баланс:</b> <tg-spoiler>{user_balance} ₽</tg-spoiler>
➖➖➖➖➖➖➖➖
<b>⏸ Запуск бота:</b>{bot_start_date}
<b>📆 Текущее время:</b>20{dt.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%y-%m-%d %H:%M')}
🗓 Бот работает <b>{farq.days}</b> дней
""",reply_markup=ortga_to_main)


@dp.callback_query_handler(text="sts")
async def bot_stat(call: types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    with open("middlewares/banned_users.txt", "r") as file:
        user_ids = file.read()
        user_ids = user_ids.split("/")
    print(user_ids)
    for user_id in user_ids:
        if user_id == '':
            user_ids.remove('')
        
    blocked = len(user_ids)
    unblocked = int(db.count_users()[0]) - int(blocked)
    users = db.select_all_users()
    bot_start_date = dt.date(2023, 8, 25)
    farq = dt.date.today() - bot_start_date
    await call.message.answer(f"<b>📊 Статистика бота</b>\n\n"
                         f"<b>✅ Активно:</b> {unblocked}\n"
                         f"<b>❌ Бан:</b> {blocked}\n"
                         f"<b>🔰 Всего:</b> {blocked+unblocked}\n"
                         f"➖➖➖➖➖➖➖➖\n"
                         f"<b>⏸ Запуск бота:</b> {bot_start_date}\n"
                         f"<b>📆 Текущее время:</b> 20{dt.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%y-%m-%d %H:%M')}\n"
                         f"🗓Бот работает <b>{farq.days}</b> дней",reply_markup=ortga_to_main)
@dp.message_handler(text_contains = "/admin")
async def find_player_with_name(message: types.Message,state:FSMContext):
    await message.answer("Нажмите!",reply_markup=admin_tugma)



@dp.callback_query_handler(text="admin_panel")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    
    await call.message.answer("✋Здравствуйте, пожалуйста, подождите, чтобы узнать, есть ли у вас доступ к панели администратора... ")
    sleep(0.5)
    user_id = call.from_user.id
    for admin in ADMINS:
        if int(admin) == int(user_id):

            a = True
            break

        else:
            
            a = False

    if a:
        await call.message.answer("✅Вы подтверждены как администратор!",reply_markup=panel_tugma)
    else:
        await call.message.answer("❌К сожалению, вы не можете получить доступ к панели администратора!")

@dp.callback_query_handler(text="rek_user_message")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("📩Реклама и 👤Сообщение пользователю",reply_markup=tugmasi)
@dp.callback_query_handler(text="rek_xb")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("📩 Реклама",reply_markup=tugmasi_rek)

@dp.callback_query_handler(text="user_xb")
async def adminusermsg(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("👤 Сообщение пользователю",reply_markup=tugmasi_user)









@dp.callback_query_handler(text="oddiy_xb_rek")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("✍️Присылайте мне новости!",reply_markup=ortga_to_panel)

    await state.set_state("xabar")
@dp.message_handler(state="xabar",content_types=["any"])
async def xb_func(message:types.Message,state:FSMContext):
    await state.finish()
    users = db.select_all_users()

    message_text = message.text
    count = 0 
    for user in users:
        user_id = user[0]
        try: 
            await bot.send_message(chat_id=user_id, text=message_text)
            sleep(0.05)
        except:
            count+=1
    await message.answer(f"🤖У бота {len(users)}подписчиков:\n ◾️{count} пользователи заблокировали бота, поэтому сообщение не было отправлено!\n ◽️Сообщение отправлено на {int(len(users))-int(count) } пользователи",reply_markup=ortga_to_panel)


@dp.callback_query_handler(text="forward_xb_rek")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()

    await call.message.answer("💬Oтправте мне пересланное сообщение!",reply_markup=ortga_to_panel)

    await state.set_state("frward_xb")
@dp.message_handler(state="frward_xb",content_types=["any"])
async def send_to_me(message:types.Message,state:FSMContext):
    await state.finish()

    users = db.select_all_users()
    message_text = message.text
    count = 0
    for user in users:
        user_id = user[0]
        try: 

            await bot.forward_message(chat_id=user_id, from_chat_id=ADMINS[0], message_id=message.message_id)
            sleep(0.005)
        except Exception as e:
            count+=1
            print(e)
    await message.answer(f"🤖У бота {len(users)}подписчиков:\n ◾️{count} пользователи заблокировали бота, поэтому сообщение не было отправлено!\n ◽️Сообщение отправлено на {int(len(users))-int(count) } пользователи",reply_markup=ortga_to_panel)
    await state.finish()




@dp.callback_query_handler(text="oddiy_xb_user")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()

    await call.message.answer("🆔Введите идентификационный номер пользователя:",reply_markup=ortga_to_panel)

    await state.set_state("xabar_user_id")

@dp.message_handler(state="xabar_user_id")
async def xb_user_id(message:types.Message,state:FSMContext):
    await state.update_data({f"{message.from_user.id}":message.text})

    await message.answer("✍️Хорошо, теперь пришлите мне текст сообщения!",reply_markup=ortga_to_panel)

    await state.set_state("xabar_007")
@dp.message_handler(state="xabar_007")
async def xb_hammaga(message:types.Message,state:FSMContext):
    state_data = await state.get_data(f"{message.from_user.id}")
    message_text = message.text
    user_id = state_data.get(f"{message.from_user.id}")
    await state.finish()
    print(user_id)
    try:
        await bot.send_message(chat_id=user_id, text=message_text)
        await message.answer(f"🤖Вы отправили сообщение пользователю {user_id} на боте:\n ◽️{user_id} было отправлено сообщение, он не заблокировал бота",reply_markup=ortga_to_panel)

    except Exception as e:
        await message.answer(f"🤖Вы отправили сообщение пользователю {user_id} в боте:\n ◾️Сообщение не может быть отправлено, так как пользователь с {user_id} заблокировал бота!",reply_markup=ortga_to_panel)
        print(e)

@dp.callback_query_handler(text="forward_xb_user")
async def send_ad_to_all__(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()

    await call.message.answer("🆔Введите идентификационный номер пользователя:",reply_markup=ortga_to_panel)

    await state.set_state("xb_frwrd_user_id")

@dp.message_handler(state="xb_frwrd_user_id")
async def player_speed(message:types.Message,state:FSMContext):
    await state.update_data({f"{message.from_user.id}":message.text})

    await message.answer("✍️Хорошо, теперь пришлите мне текст сообщения!",reply_markup=ortga_to_panel)

    await state.set_state("xabar_007_user")
@dp.message_handler(state="xabar_007_user")
async def send_to_all_(message:types.Message,state:FSMContext):
    state_data = await state.get_data(f"{message.from_user.id}")
    message_text = message.text
    await state.finish() 

    user_id = state_data.get(f"{message.from_user.id}")
    try:
        await bot.forward_message(chat_id=user_id, from_chat_id=ADMINS[0], message_id=message.message_id)
        await message.answer(f"🤖Вы отправили сообщение пользователю {user_id} на боте:\n ◽️{user_id} было отправлено сообщение, он не заблокировал бота",reply_markup=ortga_to_panel)

    except:
        await message.answer(f"🤖Вы отправили сообщение пользователю {user_id} в боте:\n ◾️Сообщение не может быть отправлено, т.к. пользователь {user_id} заблокировал бота!",reply_markup=ortga_to_panel)


              
@dp.callback_query_handler(text="new_channel")
async def send_ad_to_all(call: types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("<b>✍️Отправьте мне хорошего пользователя канала!</b>\n\n<i>*Не забывайте, что символ @ не должен появляться в имени пользователя канала!</i>",reply_markup=ortga_to_panel)

    await state.set_state("channels")
@dp.message_handler(state="channels")
async def deleteAllChannels(message:types.Message,state:FSMContext):
    with open("data/channels.txt","a+") as file:
        channels = file.read()
        channels+=f",{message.text}"
        file.write(channels)
    await message.answer("✅Ваш канал успешно добавлен!",reply_markup=ortga_to_panel)
    
    await state.finish()



@dp.callback_query_handler(text="del_all_channels")
async def player_speed(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    with open("data/channels.txt","w+") as file:
        file.write("")
    await call.message.answer("✅Все каналы удалены из списка",reply_markup=ortga_to_panel)
    
@dp.callback_query_handler(text="channels_list")
async def list_channels(call:CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    with open("data/channels.txt","r") as file:
        read_file = file.read()
        read_file_list = read_file.split(",")
        matn = ""
        count = 0
        for channel in read_file_list:

            if channel!="":
                count+=1
                matn+=f"\n      {count}.👉@{channel}👈"

        await call.message.answer(f"📡Список каналов: {matn}",reply_markup=ortga_to_panel)







@dp.callback_query_handler(text="bot_off")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.answer(cache_time=30)
    await call.message.answer("❌Хорошo админ-бот viklyuchon.",reply_markup=ortga_to_panel)
    with open("middlewares/bot_stop.txt","w") as file:
        file.write("0")
@dp.callback_query_handler(text="bot_on")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("✅Включен хороший админ-бот.",reply_markup=ortga_to_panel)
    with open("middlewares/bot_stop.txt","w") as file:
        file.write("1")
@dp.callback_query_handler(text="ban_man")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🆔Введите идентификационный номер пользователя:",reply_markup=ortga_to_panel)
    await state.set_state("to_ban_user_id")
@dp.message_handler(state="to_ban_user_id")
async def banMAN(message:types.Message,state:FSMContext):
    user_id = message.text
    with open("middlewares/banned_users.txt","r+") as file:
        idlar = file.read()
        idlar = idlar.split("/")
        if str(user_id) in idlar:
            await message.answer("🚷Пользователь уже забанен!",reply_markup=ortga_to_panel)
        else:
            file.write(f"{user_id}/")
            await message.answer("🚷Пользователь забанен",reply_markup=ortga_to_panel)
            await bot.send_message(chat_id=user_id,text="❌Вас забанили в боте")


    
    await state.finish()
@dp.callback_query_handler(text="unban_man")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🆔Введите идентификационный номер пользователя:",reply_markup=ortga_to_panel)
    await state.set_state("to_unban_user_id")

@dp.message_handler(state="to_unban_user_id")
async def banMAN(message:types.Message,state:FSMContext):
    user_id = message.text
    with open("middlewares/banned_users.txt","r") as file:
        file_data = file.read()
        user_ids = file_data.split("/")
        for user_id1 in user_ids:
            if str(user_id1) == str(user_id):
                a = True
                break
            else:
                a = False

        if a:

            user_ids.remove(user_id)
            await bot.send_message(chat_id=user_id,text=f"Вам забанен бот.")
            await message.answer("✅Хорошo пользователь забанен!",reply_markup=ortga_to_panel)
        else:
            await message.answer("❌Пользователь раньше не был рабом!",reply_markup=ortga_to_panel)     
        matn = ""
        for user_id_new in user_ids:
            matn+=f"{user_id_new}/"
        print(matn)
    with open("middlewares/banned_users.txt","w") as file:

        file.write(matn)
    await state.finish()





@dp.callback_query_handler(text="unban_men")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("✅Xorosho",reply_markup=ortga_to_panel)
    with open("middlewares/banned_users.txt","w") as file:
        pass 
@dp.callback_query_handler(text="del_channel")
async def banMan(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("📛Войти на канал пользователь (@ не участвует):",reply_markup=ortga_to_panel)
    await state.set_state("channel_username")
@dp.message_handler(state="channel_username")
async def DelChannel(message:types.Message,state:FSMContext):
    with open("data/channels.txt","r") as file:
        file_data = file.read()
        channel_users = file_data.split(",")

        for channel_user in channel_users:
            if str(channel_user) == str(message.text):
                a = True

                channel_users.remove(channel_user)
                break
            else:
                a = False
                print(channel_user,message.text)

        if a:
            await message.answer("➖Хорошo канал удален из списка",reply_markup=ortga_to_panel)
            matn = ""
            with open("data/channels.txt","w") as file:
                for channel_user in channel_users:
                    matn+=f",{channel_user}"


        else:
            await message.answer("❌Этот канал недоступен в списке",reply_markup=ortga_to_panel)
        await state.finish()


 
@dp.callback_query_handler(text="channel_tools")
async def channel__tools(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🤙Выбери один!",reply_markup=channel_tools)

@dp.callback_query_handler(text="ban_tools")
async def ban__tools(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🤙Выбери один!",reply_markup=ban_tools)
@dp.callback_query_handler(text="bot_on_off")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    await call.message.answer("🤙Выбери один!",reply_markup=bot_on_off)
@dp.callback_query_handler(text="balance_api")
async def data_dls_tools(call:types.CallbackQuery,state:FSMContext):
    await call.answer(cache_time=30)
    await call.message.delete()
    balance = await get_balance(api_token=token) 
    balance = balance.balance
    await call.message.answer(f"💰 Balans: {balance}₽ ",reply_markup=ortga_to_panel)

