from aiogram import types
from aiogram.types import ParseMode
from aiogram.utils.markdown import text, italic, bold


async def stand_by(message: types.Message):
    msg = text(
        italic('Я все еще жду ваших указаний'),
        bold('Узнайте о моих возможностях с помощью команды /help'),
        sep='\n')
    await message.answer(msg, parse_mode=ParseMode.MARKDOWN)
