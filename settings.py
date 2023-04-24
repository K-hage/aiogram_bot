from pathlib import Path

from envparse import env

BASE_DIR = Path(__file__).resolve().parent

if (env_path := BASE_DIR.joinpath('.env')) and env_path.is_file():
    env.read_envfile(env_path)

TOKEN = env.str('TOKEN')

COMMANDS = [
    '/start',
    '/help',
    '/weather',
    '/weather <Населенный пункт>',
    '/currency',
    '/cuteanimals',
]

API_WEATHER_TOKEN = env.str('API_WEATHER_TOKEN')

URL_API_WEATHER = 'https://api.openweathermap.org/data/2.5/weather'

LANGUAGE_FOR_WEATHER = 'ru'

UNITS_FOR_WEATHER = 'metric'

URL_PARSE_PICTURES = 'https://klike.net/2879-kartinki-milyh-zhivotnyh-35-foto.html'

PICTURES = [
    'https://klike.net/uploads/posts/2020-03/1585127518_1.jpg',
    'https://klike.net/uploads/posts/2020-03/1585127496_2.jpg',
    'https://klike.net/uploads/posts/2020-03/1585127532_4.jpg',
]
