from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

from http_client import WOMHttpClient
from config import Settings

router = Router()


async def initialize_web_client():
    web_client = WOMHttpClient('https://api.openweathermap.org', Settings.OWM_API_KEY)
    return web_client


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer('Что-то типа тут будет, это не последняя версия')


@router.message(F.text)
async def forecast_handler(message: Message):
    web_client = await initialize_web_client()
    value = str(await web_client.get_city_forecast(message.text))
    await message.answer(value)

