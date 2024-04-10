from aiohttp import ClientSession
from async_lru import alru_cache
from config import Settings

from data.City import City
from data.Forecast import Forecast


class HTTPClient:
    def __init__(self, base_url: str, api_key: str):
        self._session = ClientSession(
            base_url=base_url,
            headers={
                'appid': api_key,
            }
        )


class WOMHttpClient(HTTPClient):

    @alru_cache
    async def get_city_latitude(self, city):
        async with self._session.get('/geo/1.0/direct', params={'q': city, 'appid': Settings.OWM_API_KEY}) as response:
            result = await response.json()

            city_data = City.parse_obj(dict(result[0]))

            return city_data

    @alru_cache
    async def get_city_forecast(self, city: str):

        city_data = await self.get_city_latitude(city)

        async with self._session.get(
                url=f'/data/2.5/weather',
                params={
                    'lat': city_data.lat,
                    'lon': city_data.lon,
                    'appid': Settings.OWM_API_KEY,
                    'lang': 'ru',
                    'units': 'metric'
                }
        ) as response:
            result = await response.json()

            forecast = Forecast(
                description=result['weather'][0]['description'],
                temperature=result['main']['temp'],
                feels_like=result['main']['feels_like'],
                wind_speed=result['wind']['speed']
            )

            return forecast

