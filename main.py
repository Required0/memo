import asyncio
from aiogram import Bot, Dispatcher
from app.rout import rout
from aiogram.types import BotCommand 
from aiogram.methods.set_my_commands import SetMyCommands 
from config import tk
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

bot = Bot(token=tk)
dp = Dispatcher()


async def set_default_commands(bt: bot):
    # Команды, которые будут отображаться в меню
    commands = [
        BotCommand(command="start", description="🚀 Запустить бота"),
        BotCommand(command="help", description="ℹ️ Помощь по боту"),
    ]
    # Отправляем список команд в Telegram
    await bot.set_my_commands(commands)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(rout)
    await set_default_commands(bot)
    await dp.start_polling(bot)



if  __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('бот выключен')