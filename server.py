from aiogram import Dispatcher, Bot
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

from handlers import cmd_start, stand_by, cmd_help, cmd_cancel, cmd_weather, cmd_cute_animals
from settings import TOKEN


async def register_handles(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'])
    dp.register_message_handler(cmd_help, commands=['help'], state='*')
    dp.register_message_handler(cmd_weather, commands=['weather'], state='*')
    dp.register_message_handler(cmd_cancel, commands=['cancel'], state='*')
    dp.register_message_handler(cmd_cute_animals, commands=['cuteanimals'], state='*')
    dp.register_message_handler(stand_by, content_types=['any'])


def main() -> None:
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    executor.start_polling(dp, skip_updates=True, on_startup=register_handles)
