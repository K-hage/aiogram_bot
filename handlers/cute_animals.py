import random

from aiogram import types

import settings
from utils.parse_picture import get_image_links


async def cmd_cute_animals(message: types.Message):
    pictures = await get_image_links(settings.URL_PARSE_PICTURES)
    photo = random.choice(pictures)
    await message.answer_photo(photo)
