
from aiogram import Bot, Dispatcher, executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup

API_TOKEN = '6091793914:AAG5ZV1IJyGiqy3Elj8j8L8IstGoy2VrOqQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

#продукты
iphones = {
     'Iphone 14': 63400,
     'Iphone 14 pro': 80900,
     'Iphone 14 pro max': 102000,
     'Iphone 13': 53400,
     'Iphone 13 pro': 75900,
     'Iphone 13 pro max': 83000,
     'Iphone 12': 45400,
     'Iphone 12 pro': 60900,
     'Iphone 12 pro max': 70000
 }

# Клавиатуры

# Главная клавиатура
kb_btns = [
    [KeyboardButton(text='Цена'), KeyboardButton(text='О нас')],
]
kb_main = ReplyKeyboardMarkup(keyboard=kb_btns, resize_keyboard=True)

#klava vibora apple
kb_btns_models = []
for key in iphones:
   btn = [KeyboardButton(text=key, callback_data=key)]
   kb_btns_models.append(btn)
kb_models = InlineKeyboardMarkup(inline_keyboard=kb_btns_models)
   

# Хендлеры
async def start_handler(message):
    await message.answer('Привет! Я бот, умею ...', reply_markup=kb_main) 

async def about_handler(message):
    await message.answer('Мы - компания, Kooch')

async def price_handler(message):
    await message.answer('В наличии вот такие смартфоны, марки Apple', reply_markup=kb_models)

async def show_price_handler(callback):
    await callback.message.answer(iphones[callback.data])

# Регистрация хендлеров
dp.register_message_handler(start_handler, commands=['start'])
dp.register_message_handler(about_handler, lambda mes: mes.text == 'О нас')
dp.register_message_handler(price_handler, lambda mes: mes.text == 'Цена')
dp.register_callback_query_handler(show_price_handler, lambda cb: cb.data.startswith('Iphone'))

# Запуск бота
executor.start_polling(dp, skip_updates=True)



