from aiogram.types import CallbackQuery,Message,ParseMode
from aiogram.dispatcher import FSMContext
from keyboards.inline.admin_keys import amazon,discord,avito,samokat,sbermarket,ebay,tinder,instagram,facebook,microsoft,apple,paypal,steam,telegram,uber,twitter,whatsapp,vkontakte,tiktok,yandex,gmail
from keyboards.default.buttons import numbers_list_one_admin,ortga_to_main,ortga_to_panel
from aiogram import Bot, Dispatcher, executor, types 
from time import sleep
import datetime as dt
import pytz
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from loader import dp,db,bot,balance,price
def get_keyboard(product):
    if product=="amazon":
        return amazon
    elif product=="instagram":
        return instagram
    elif product=='facebook':
        return facebook
    elif product=='discord':
        return discord
    elif product=='avito':
        return avito
    elif product=='samokat':
        return samokat
    elif product=='sbermarket':
        return sbermarket
    elif product=='ebay':
        return ebay
    elif product=='tinder':
        return tinder
    elif product=='apple':
        return apple
    elif product=='microsoft':
        return microsoft
    elif product=='steam':
        return steam
    elif product=='telegram':
        return telegram
    elif product=='twitter':
        return twitter
    elif product=='whatsapp':
        return whatsapp
    elif product=='uber':
        return uber
    elif product=='vkontakte':
        return vkontakte
    elif product=='tiktok':
        return tiktok
    elif product=='google':
        return gmail
    elif product=='yandex':
        return yandex
    else:
        return numbers_list_one_admin
@dp.callback_query_handler(text='number_prices')
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите услугу, которую необходимо изменить!",reply_markup=numbers_list_one_admin)
@dp.callback_query_handler(text="instagram_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=instagram)

@dp.callback_query_handler(text="facebook_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=facebook)

@dp.callback_query_handler(text="amazon_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=amazon)

@dp.callback_query_handler(text="discord_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=discord)

@dp.callback_query_handler(text="avito_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=avito)

@dp.callback_query_handler(text="samokat_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=samokat)

@dp.callback_query_handler(text="sbermarket_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=sbermarket)

@dp.callback_query_handler(text="ebay_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=ebay)

@dp.callback_query_handler(text="tinder_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=tinder)

@dp.callback_query_handler(text="microsoft_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=microsoft)

@dp.callback_query_handler(text="apple_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=apple)



@dp.callback_query_handler(text="paypal_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=paypal)

@dp.callback_query_handler(text="steam_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=steam)

@dp.callback_query_handler(text="telegram_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=telegram)

@dp.callback_query_handler(text="uber_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=uber)

@dp.callback_query_handler(text="twitter_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=twitter)

@dp.callback_query_handler(text="whatsup_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=whatsapp)

@dp.callback_query_handler(text="vkontakte_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=vkontakte)

@dp.callback_query_handler(text="tiktok_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=tiktok)

@dp.callback_query_handler(text="gmail_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=gmail)

@dp.callback_query_handler(text="yandex_edit")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("✏️Выберите страну, в которой необходимо изменить цену!",reply_markup=yandex)
@dp.callback_query_handler(lambda c: c.data.startswith('admin:'))
async def return_number(call: types.CallbackQuery):
    await call.message.delete()
    datas = call.data.split(':')
    country = datas[1]
    product = datas[2]
    number_price = price.get_price(f'{country}:{product}')
    user_balance = balance.get_balance(user_id=call.from_user.id)

    get_number = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("📝 Редактировать",callback_data=f"edit:{country}:{product}:{number_price}"),
    ],
    [
        InlineKeyboardButton("🔙 Hазад", callback_data=f"back_admin:{product}")
    ]
])
    await call.message.answer(f"""
📌 Вы выбрали

🌐 Сервис: {product.capitalize()}
🔄 Страна: {country.capitalize()}
💸 Tекущий cумма: {number_price} ₽


""",reply_markup=get_number)
@dp.callback_query_handler(lambda c: c.data.startswith('edit:'))
async def return_number(call: types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    datas = call.data.split(':')
    country = datas[1]
    product = datas[2]
    number_price_latest = datas[3]
    number_price = price.get_price(f'{country}:{product}')
    await call.message.answer(f'''
<b>✍️Введите новую сумму:</b>


🌐 Сервис: {product.capitalize()}
🔄 Страна: {country.capitalize()}
💸 Tекущий cумма: {number_price} ₽

''',reply_markup=ortga_to_panel)
    await state.update_data({f'datas_{call.from_user.id}':datas})
    await state.set_state('get_summa')
@dp.message_handler(state='get_summa')
async def return_number(message: types.Message,state:FSMContext):
    
    state_data = await state.get_data()
    datas = state_data.get(f'datas_{message.from_user.id}')
    print(datas)
    price.save_price(f'{datas[1]}:{datas[2]}',f'{message.text}')
    number_price = price.get_price(f'{datas[1]}:{datas[2]}')
    await state.finish()
    await message.answer(f"""
✅ Сохранено

🌐 Сервис: {datas[2].capitalize()}
🔄 Страна: {datas[1].capitalize()}
💸 Предыдущая сумма: {datas[3]} ₽
💸 Tекущий cумма: {number_price} ₽
""",reply_markup=ortga_to_panel)
@dp.callback_query_handler(lambda c: c.data.startswith('back_admin:'))
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    keyboard_name = get_keyboard(call.data.split(':')[1])
    await call.message.answer("🔙 Вернулся",reply_markup=keyboard_name)

@dp.callback_query_handler(text="users_settings")
async def stats_users(call:types.CallbackQuery,state:FSMContext):
    await call.message.delete()
    await call.message.answer("🆔Чтобы настроить счет, введите идентификационный номер счета:",reply_markup=ortga_to_panel)
    await state.set_state("next_state")
    
@dp.message_handler(state="next_state")
async def stats_users(message:types.Message,state:FSMContext):
    await state.finish()
    user = message.text
    try:
        user_data = await bot.get_chat(user)
    except: 
        await message.answer("🤷🏻‍♂️ Такой пользователь недоступен в боте",reply_markup=ortga_to_panel)
        return 
    buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="➕ Счет",callback_data=f"plus:{user}"),
        InlineKeyboardButton(text="➖ Счет",callback_data=f"minus:{user}")        

    ],
    [
        InlineKeyboardButton(text="🔄 Обновить",callback_data=f"refresh:{user}")        

    ],
    [
        InlineKeyboardButton(text="🔙 ",callback_data="ortga_to_panel")        
    ]
])
    bot_start_date = dt.date(2023, 8, 25)
    farq = dt.date.today() - bot_start_date
    user_balance = balance.get_balance(user_id=user)
    await message.answer(f"""
<b>📛 User имя:</b> <i>{user_data.first_name}</i>
<b>✊ User имя пользователя:</b> @{user_data.username}
<b>🆔 User идентификатор:</b> <code>{user_data.id}</code>
<b>💰 User баланс:</b> <tg-spoiler>{user_balance} ₽</tg-spoiler>
➖➖➖➖➖➖➖➖
<b>⏸ Запуск бота:</b>{bot_start_date}
<b>📆 Текущее время:</b>20{dt.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%y-%m-%d %H:%M')}
🗓 Бот работает <b>{farq.days}</b> дней
""",reply_markup=buttons)

@dp.callback_query_handler(text_contains="minus")
async def stats_users(call:types.CallbackQuery,state:FSMContext):
    user = call.data.replace("minus:","")
    await call.message.answer("➖ Чтобы вычитание счет, введите ₽:",reply_markup=ortga_to_panel)
    await state.update_data({f"{call.from_user.id}":f"{user}"})
    await state.set_state("min_balance")
@dp.callback_query_handler(text_contains="refresh")
async def stats_users(call:types.CallbackQuery,state:FSMContext):
    user = call.data.replace("refresh:","")
    try:
        user_data = await bot.get_chat(user)
    except: 
        await call.message.answer("🤷🏻‍♂️ Такой пользователь недоступен в боте",reply_markup=ortga_to_panel)
        return 
    buttons = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="➕ Счет",callback_data=f"plus:{user}"),
        InlineKeyboardButton(text="➖ Счет",callback_data=f"minus:{user}")        

    ],
    [
        InlineKeyboardButton(text="🔄 Обновить",callback_data=f"refresh:{user}")        

    ],
    [
        InlineKeyboardButton(text="🔙 Назад",callback_data="ortga_to_panel")        
    ]
])
    bot_start_date = dt.date(2023, 8, 25)
    farq = dt.date.today() - bot_start_date
    user_balance = balance.get_balance(user_id=user)
    try:
        await call.message.edit_text(f"""
<b>📛 User имя:</b> <i>{user_data.first_name}</i>
<b>✊ User имя пользователя:</b> @{user_data.username}
<b>🆔 User идентификатор:</b> <code>{user_data.id}</code>
<b>💰 User баланс:</b> <tg-spoiler>{user_balance} ₽</tg-spoiler>
➖➖➖➖➖➖➖➖
<b>⏸ Запуск бота:</b>{bot_start_date}
<b>📆 Текущее время:</b>20{dt.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%y-%m-%d %H:%M')}
🗓 Бот работает <b>{farq.days}</b> дней
""",reply_markup=buttons)   
    except:
        await call.answer("❌ Hech narsa o'zgarmadi!")
@dp.message_handler(state="min_balance")
async def stats_users(message:types.Message,state:FSMContext):
    state_data = await state.get_data()
    user = state_data.get(f"{message.from_user.id}")
    try:
        amount = float(message.text)
    except: 
        await message.answer("🔢Пожалуйста, просто введите номер!",reply_markup=ortga_to_panel)
        await state.set_state("next_state_2")
        return

    try:
        balance.minus_balance(user_id=user,amount=float(message.text))
        try:
            user_data = await bot.get_chat(user)
        except: 
            await message.answer("🤷🏻‍♂️ Такой пользователь недоступен в боте",reply_markup=ortga_to_panel)
            return 
        buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Счет",callback_data=f"plus:{user}"),
            InlineKeyboardButton(text="➖ Счет",callback_data=f"minus:{user}")        

        ],
        [
            InlineKeyboardButton(text="🔄 Обновить",callback_data=f"refresh:{user}")        

        ],
        [
            InlineKeyboardButton(text="🔙 Назад",callback_data="ortga_to_panel")        
        ]
    ])
        bot_start_date = dt.date(2023, 8, 25)
        farq = dt.date.today() - bot_start_date
        user_balance = balance.get_balance(user_id=user)
        await message.answer(f"""
    <b>📛 User имя:</b> <i>{user_data.first_name}</i>
    <b>✊ User имя пользователя:</b> @{user_data.username}
    <b>🆔 User идентификатор:</b> <code>{user_data.id}</code>
    <b>💰 User баланс:</b> <tg-spoiler>{user_balance} ₽</tg-spoiler>
    ➖➖➖➖➖➖➖➖
    <b>⏸ Запуск бота:</b>{bot_start_date}
    <b>📆 Текущее время:</b>20{dt.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%y-%m-%d %H:%M')}
    🗓 Бот работает <b>{farq.days}</b> дней
    """,reply_markup=buttons)
    except:
        await message.answer("""
🤷🏻‍♂️я думаю, вы неправильно ввели идентификатор пользователя!

💰Пользовательский баланс не вычитaлся!
♻️ Попробуйте еще раз!
""",reply_markup=ortga_to_panel)
    await state.finish()


@dp.callback_query_handler(text_contains="plus")
async def stats_users(call:types.CallbackQuery,state:FSMContext):
    user = call.data.replace("plus:","")
    await call.message.answer("➕ Чтобы добавить счет, введите ₽:",reply_markup=ortga_to_panel)
    await state.update_data({f"{call.from_user.id}":f"{user}"})
    await state.set_state("pls_balance")
    
@dp.message_handler(state="pls_balance")
async def stats_users(message:types.Message,state:FSMContext):
    state_data = await state.get_data()
    user = state_data.get(f"{message.from_user.id}")
    try:
        amount = float(message.text)
    except: 
        await message.answer("🔢Пожалуйста, просто введите номер!",reply_markup=ortga_to_panel)
        await state.set_state("next_state_2")
        return

    try:
        balance.update_balance(user_id=user,amount=float(message.text))
        try:
            user_data = await bot.get_chat(user)
        except: 
            await message.answer("🤷🏻‍♂️ Такой пользователь недоступен в боте",reply_markup=ortga_to_panel)
            return 
        buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Счет",callback_data=f"plus:{user}"),
            InlineKeyboardButton(text="➖ Счет",callback_data=f"minus:{user}")        

        ],
        [
            InlineKeyboardButton(text="🔄 Обновить",callback_data=f"refresh:{user}")        

        ],
        [
            InlineKeyboardButton(text="🔙 Назад",callback_data="ortga_to_panel")        
        ]
    ])
        bot_start_date = dt.date(2023, 8, 25)
        farq = dt.date.today() - bot_start_date
        user_balance = balance.get_balance(user_id=user)
        await message.answer(f"""
    <b>📛 User имя:</b> <i>{user_data.first_name}</i>
    <b>✊ User имя пользователя:</b> @{user_data.username}
    <b>🆔 User идентификатор:</b> <code>{user_data.id}</code>
    <b>💰 User баланс:</b> <tg-spoiler>{user_balance} ₽</tg-spoiler>
    ➖➖➖➖➖➖➖➖
    <b>⏸ Запуск бота:</b>{bot_start_date}
    <b>📆 Текущее время:</b>20{dt.datetime.now(pytz.timezone('Asia/Tashkent')).strftime('%y-%m-%d %H:%M')}
    🗓 Бот работает <b>{farq.days}</b> дней
    """,reply_markup=buttons)
        

    except:
        await message.answer("""
🤷🏻‍♂️я думаю, вы неправильно ввели идентификатор пользователя!

💰Пользовательский баланс не пополнился!
♻️ Попробуйте еще раз
""",reply_markup=ortga_to_panel)
    await state.finish()