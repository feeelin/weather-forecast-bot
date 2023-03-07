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

    await bot.send_message(user_id, text=f'Привет, {user_name}! \nЯ помогу тебе узнать погоду на сегодня, введи '
                                         'город!')


@dp.message_handler(content_types='text')
async def text_handler(message: types.message):
    result = findCity(message.text)

    if result:
        data = get_forecast(result)
        await message.reply(f'В городе {message.text} сегодня {data["conditions"]}, температура воздуха '
                            f'{data["temp"]}')
    else:
        await message.reply(f'Город {message.text} не найден')


if __name__ == '__main__':
    executor.start_polling(dp)