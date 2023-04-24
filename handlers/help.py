from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, italic

from settings import COMMANDS


async def cmd_help(message: types.Message):
    msg = text(italic('Я могу ответить на следующие команды:'),
               '\n'.join(COMMANDS), sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)
