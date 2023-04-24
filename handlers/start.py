from aiogram import types


async def cmd_start(message: types.Message):
    user_full_name = message.from_user.full_name
    await message.answer(f"Привет, {user_full_name}!")
