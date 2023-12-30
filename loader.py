from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.sqlite import Database,UserBalanceDB,ProductPriceDB,PaymentChecker
from data import config

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database(path_to_db="data/main.db")
balance = UserBalanceDB("data/user_balances.db")
price = ProductPriceDB("data/product_prices.db")
paymentchecker = PaymentChecker("data/payment_checker.db")
# price.save_price("canada:instagram",1)