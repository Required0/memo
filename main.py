import asyncio
from app.rout import rout
from aiogram.types import BotCommand 
from aiogram.methods.set_my_commands import SetMyCommands 
from config import bot, dp
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


async def set_default_commands(bt: bot):
    # Команды, которые будут отображаться в меню
    commands = [
        BotCommand(command="start", description="🚀 Запустить бота"),
        BotCommand(command="tasks", description="📝 Мои напоминания"),
        BotCommand(command="timezone", description="⏳ Установить/Изменить часовой пояс"),
        BotCommand(command="help", description="ℹ️ Помощь по боту"),
    ]
    # Отправляем список команд в Telegram
    await bot.set_my_commands(commands)



async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    dp.include_router(rout)
    await set_default_commands(bot)

    try:
        await dp.start_polling(bot) # Основной цикл бота
    finally:
        await bot.session.close()
        
    



if  __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('бот выключен')
        