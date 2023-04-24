from aiogram import types
from aiogram.dispatcher import FSMContext


async def cmd_cancel(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Команда отменена')
