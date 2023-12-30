from aiogram.types import CallbackQuery,Message,ParseMode
from aiogram.dispatcher import FSMContext
from keyboards.default.instagram_facebook import instagram,facebook
from keyboards.default.amazon_discord import amazon,discord
from keyboards.default.avito_samokat_sbermarket import avito,samokat,sbermarket
from keyboards.default.ebay_tinder import ebay,tinder
from keyboards.default.microsoft_apple import microsoft,apple
from keyboards.default.paypal_steam import paypal,steam
from keyboards.default.telegram_uber import telegram,uber
from keyboards.default.twitter_whatsup import twitter,whatsapp
from keyboards.default.vkontakte_tiktok import vkontakte,tiktok
from keyboards.default.yandex_gmail import yandex,gmail
from keyboards.default.buttons import numbers_list_one
from aiogram import Bot, Dispatcher, executor, types 
from time import sleep
from loader import dp,db,bot
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
    elif product=='gmail':
        return gmail
    elif product=='yandex':
        return yandex
    else:
        return numbers_list_one



@dp.callback_query_handler(text="instagram")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=instagram)

@dp.callback_query_handler(text="facebook")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=facebook)

@dp.callback_query_handler(text="amazon")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=amazon)

@dp.callback_query_handler(text="discord")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=discord)

@dp.callback_query_handler(text="avito")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=avito)

@dp.callback_query_handler(text="samokat")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=samokat)

@dp.callback_query_handler(text="sbermarket")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=sbermarket)

@dp.callback_query_handler(text="ebay")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=ebay)

@dp.callback_query_handler(text="tinder")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=tinder)

@dp.callback_query_handler(text="microsoft")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=microsoft)

@dp.callback_query_handler(text="apple")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=apple)



@dp.callback_query_handler(text="paypal")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=paypal)

@dp.callback_query_handler(text="steam")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=steam)

@dp.callback_query_handler(text="telegram")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=telegram)

@dp.callback_query_handler(text="uber")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=uber)

@dp.callback_query_handler(text="twitter")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=twitter)

@dp.callback_query_handler(text="whatsup")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=whatsapp)

@dp.callback_query_handler(text="vkontakte")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=vkontakte)

@dp.callback_query_handler(text="tiktok")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=tiktok)

@dp.callback_query_handler(text="gmail")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=gmail)

@dp.callback_query_handler(text="yandex")
async def select_country_instagram(call:types.CallbackQuery):
    await call.answer(cache_time = 30)
    await call.message.delete()
    await call.message.answer("❗️ Выберите нужную страну!",reply_markup=yandex)
@dp.callback_query_handler(lambda c: c.data.startswith('back:'))
async def stats_users(call:types.CallbackQuery):
    await call.answer(cache_time=30)
    await call.message.delete()
    keyboard_name = get_keyboard(call.data.split(':')[1])
    await call.message.answer("🔙 Вернулся",reply_markup=keyboard_name)

