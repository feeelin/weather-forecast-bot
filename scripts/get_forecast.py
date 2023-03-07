import requests
from scripts.find_city import app_id


def get_forecast(city_id: int):
    try:
        res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                           params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': app_id})
        data = res.json()

        output = {
            'conditions': data['weather'][0]['description'],
            'temp': data['main']['temp'],
        }
        return output

    except:
        pass
