from aiogram import Bot, Dispatcher, executor, types
from time import sleep
from keyboards.default.buttons import ortga_to_main
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from loader import dp,db,bot,balance,price
import requests
from data.config import fivesimnettoken as token
from utils.get_number import get_price,get_phone,get_sms,get_country


@dp.callback_query_handler(lambda c: c.data.startswith('country:'))
async def return_number(call: types.CallbackQuery):
    call_data = call.data
    buttons = call.message.reply_markup.inline_keyboard[0]  #[0].text
    for button in buttons:
        button.callback_data == call_data
        button_text = button.text
        break
    print(button_text)
    await call.message.delete()
    datas = call.data.split(':')
    country = datas[1]
    product = datas[2]
    number_price = price.get_price(f'{country}:{product.lower()}')
    user_balance = balance.get_balance(user_id=call.from_user.id)
    remain = await get_price(api_token=token,service_=product,country=get_country(country))
    print(product,country,get_country(country))
    get_number = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton("💳 Платить",callback_data=f"pay:{country}:{product}"),
        InlineKeyboardButton("🔝 Пополнить баланс",callback_data="top_balance")

    ],
    [
        InlineKeyboardButton("🔙 Hазад", callback_data=f"back:{product}")
    ]
])
    await call.message.answer(f"""
📌 Вы выбрали

🌐 Сервис: {product.capitalize()}
🔄 Страна: {country.capitalize()}
💸 Сумма: {number_price} ₽
⛔️ Oсталось: {remain}

💰 Баланс: {user_balance} ₽
""",reply_markup=get_number)

@dp.callback_query_handler(lambda c: c.data.startswith('pay:'))
async def return_number(call: types.CallbackQuery):
    await call.message.delete()
    user_id = call.from_user.id
    datas = call.data.split(':')
    country = datas[1]
    product = datas[2]
    number_price = price.get_price(f'{country}:{product}')
    user_balance = balance.get_balance(user_id=call.from_user.id) 
    if float(user_balance)<float(number_price):
        await call.message.answer("❌ Недостаточно денег на балансе",reply_markup=ortga_to_main)
        return
    print(user_balance,number_price)
    remain = await get_price(api_token=token,service_=product,country=get_country(country))
    balance.minus_balance(user_id=user_id,amount=float(number_price))
    number = await get_phone(api_token=token,country=get_country(country),service=product)
    if number:
        buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('📩 Получить SMS',callback_data=f"sms_phone_id:{number.operation_id}:{number.number}:{number_price}"),

        ],
        [
            InlineKeyboardButton('🔙 Назад',callback_data=f"ortga_to_main")
        ]

    ])
        await call.message.answer(f"📲 Твой номер - <code>{number.number}</code>",reply_markup=buttons)
    else:

        await call.message.answer('❌На данный момент такого номера не осталось.',reply_markup=ortga_to_main)
        
@dp.callback_query_handler(lambda c: c.data.startswith('sms_phone_id:'))
async def return_number(call: types.CallbackQuery):

    user_id = call.from_user.id
    number = call.data.split(':')
    sms_code = await get_sms(api_token=token,operation_id=number[1])
    sms_code = sms_code.message
    buttons = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton('📩 Получить SMS',callback_data=f"sms_phone_id:{number[1]}:{number[2]}:{number[3]}"),

        ],
        [
            InlineKeyboardButton('🔙 Назад',callback_data=f"ortga_to_main")
        ]

    ])
    if sms_code:
        await call.message.edit_text(f'📲 Baш номер - <code>{number[2]}</code>\n🫵 Ваш смс-код: <code>{sms_code}</code>')
        await call.message.answer(f"""
✅ Номер куплен!
♻️ {number[3]}$ снято с вашего счета
🛍Спасибо за покупку
""",reply_markup=ortga_to_main) 
    else:
        await call.message.edit_text(f'📲 Baш номер - <code>{number[2]}</code>\n🫵 Ваш смс-код: ❌Hичего',reply_markup=buttons)
