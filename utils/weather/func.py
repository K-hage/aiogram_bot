import aiohttp
import marshmallow_dataclass

import settings
from utils.weather.classes import Weather


async def get_weather(city: str) -> Weather:
    """ Запрашиваем погоду в OpenWeatherApi и возвращаем ее """

    openweather_response = await _get_openweather_response(city=city)

    weather_schema = marshmallow_dataclass.class_schema(Weather)
    weather = weather_schema().load(openweather_response)
    return weather


def get_weather_answer(weather: Weather) -> str:
    """ Генерирует текст для ответа пользователю"""
    text = (
        f'В {weather.location} сегодня {weather.description}\n'
        f'Температура воздуха {weather.main.temp}\n'
        f'ощущается как {weather.main.feels_like}\n'
        f'Ветер {weather.wind.direction_wind} {weather.wind.speed} м/с\n'
        f'Возможны порывы ветра до {weather.wind.gust} м/c\n'
        f'Влажность воздуха {weather.main.humidity} %\n'
        f'Атмосферное давление {weather.main.mmHG} мм рт.ст.\n'
    )
    return text


async def _get_openweather_response(city: str) -> dict:
    url = settings.URL_API_WEATHER
    params = {
        'q': city,
        'appid': settings.API_WEATHER_TOKEN,
        'units': settings.UNITS_FOR_WEATHER,
        'lang': settings.LANGUAGE_FOR_WEATHER,
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            resp = await response.json()
            return resp
