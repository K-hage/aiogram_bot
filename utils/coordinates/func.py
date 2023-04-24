import aiohttp
import marshmallow_dataclass

from utils.coordinates.classes import Coordinates


async def get_coordinates() -> Coordinates:
    """Returns current coordinates using IP address"""
    data = await _get_ip_data()
    weather_schema = marshmallow_dataclass.class_schema(Coordinates)
    coordinates = weather_schema().load(data)
    return coordinates


async def _get_ip_data() -> dict:
    url = 'http://ipinfo.io/json'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            ip_data = await response.json()
            return ip_data
