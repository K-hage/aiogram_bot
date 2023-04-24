from aiogram import types

from utils.coordinates import get_coordinates
from utils.weather import get_weather, get_weather_answer


async def cmd_weather(message: types.Message):
    if arg := message.get_args():
        try:
            wthr = await get_weather(city=arg)
        except Exception as _ex:
            return await message.answer('Нет данных по вашему запросу')
    else:
        coord = await get_coordinates()
        wthr = await get_weather(coord.city)

    answer = get_weather_answer(wthr)
    await message.answer(answer)
