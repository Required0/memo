import asyncio
from app.rout import rout
from aiogram.types import BotCommand 
from aiogram.methods.set_my_commands import SetMyCommands 
from config import bot, dp, scheduler
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logging.getLogger('apscheduler').setLevel(logging.DEBUG)

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
    
    print(f"DEBUG: Тип scheduler перед start(): {type(scheduler)}")
    print(f"DEBUG: Значение scheduler перед start(): {scheduler}")
    
    scheduler.start() 
    print("✅ Планировщик УСПЕШНО запущен")

    try:
        await dp.start_polling(bot) # Основной цикл бота
    finally:
        print("Завершение работы: останавливаю планировщик и закрываю сессию бота...")
        scheduler.shutdown(wait=False) 
        await bot.session.close()
        print("Бот успешно остановлен.")
    



if  __name__ == '__main__':
    try:
        asyncio.run(main())
    except:
        print('бот выключен')
        