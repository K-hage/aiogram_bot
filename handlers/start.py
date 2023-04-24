from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, italic

from settings import COMMANDS


async def cmd_start(message: types.Message):
    user_full_name = message.from_user.full_name
    await message.answer(f"Привет, {user_full_name}!")
    msg = text(italic('Я могу ответить на следующие команды:'),
               '\n'.join(COMMANDS), sep='\n')
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)
