from aiogram import Bot, Dispatcher, types, executor
from scripts.get_forecast import *
from scripts.find_city import *

token = '6165297575:AAFm_5L7XHNRa1tQyozhhxfCQ6PnL8Pb1a4'
bot = Bot(token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_handler(message: types.message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ['Москва', 'Санкт-Петербург', 'Тула']

    for button in buttons:
        markup.add(button)

    await bot.send_message(user_id, text=f'Привет, {user_name}! \nЯ помогу тебе узнать погоду на сегодня.\nНажми кнопку'
                                         f' или введи город!', reply_markup=markup)


@dp.message_handler(content_types='text')
async def text_handler(message: types.message):
    result = findCity(message.text)

    if result:
        data = get_forecast(result)
        await message.reply(f'В городе {message.text} сегодня {data["conditions"]}.\nТемпература воздуха '
                            f'{int(data["temp"])}°C, ощущается как {int(data["feels_like"])}°C\n'
                            f'Скорость ветра {data["wind_speed"]} м/c')
    else:
        await message.reply(f'Город {message.text} не найден')


if __name__ == '__main__':
    executor.start_polling(dp)
