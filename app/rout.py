from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext 
from app.state import Newtask
from app import keyb as kb
import logging

rout = Router()



@rout.message(CommandStart())
async def cmd_start(mes: Message):
    logging.info(f"Получена команда /start от пользователя {mes.from_user.id}")
    user_name = mes.from_user.full_name
    await mes.answer_photo(photo="AgACAgIAAxkBAAIBeGkQWbGAb4WHs2OcxDmMsmtqAAGy3gACcw1rG4stgEgmsxMZ2x-I6QEAAwIAA3kAAzYE",
                           caption=f"Привет, {user_name}! Я помогу тебе записать самое важное и напомню обо всем, что нужно 😌 \nЖмакай на новое напоминание", reply_markup=kb.main)
   
#создание новых задач
@rout.callback_query(F.data == "newtask")
async def new_task(call:CallbackQuery, state: FSMContext):
    await state.set_state(Newtask.name_task)
    await call.answer('')
    await call.edit_message_caption(caption="О чем тебе напомнить? Напиши кратко так, как было бы понятно тебе 💚")
    await call.message.edit_reply_markup(reply_markup=None)



@rout.message(F.photo)
async def get_photo_id(message: Message):
 photo_file_id = message.photo[-1].file_id
 print(photo_file_id)


@rout.message(Command("help"))
async def help(mes: Message):
    logging.info(f"Получена команда /help от пользователя {mes.from_user.id}")
    await mes.answer('Help')





@rout.message(Newtask.name_task)
async def name_task(mes: Message, state: FSMContext):
    await state.update_data(task_s=mes.text)
    await state.set_state(Newtask.month)
    await mes.answer("ВыберИИИИИ , в какой месяц напомнить", reply_markup=kb.month)



@rout.callback_query(Newtask.month, F.data.startswith("month_"))
async def month(call: CallbackQuery, state: FSMContext): 
   callback_data_string = call.data 

   month_names_map = {
    "month_one": "Январь", "month_two": "Февраль", "month_three": "Март", "month_four": "Апрель",
    "month_five": "Май", "month_six": "Июнь", "month_seven": "Июль", "month_eight": "Август",
    "month_nine": "Сентябрь", "month_ten": "Октябрь", "month_eleven": "Ноябрь", "month_twelve": "Декабрь"
 }
   display_month_name = month_names_map[callback_data_string]
   await state.update_data(month_s=display_month_name)
   await state.set_state(Newtask.time)
   await call.answer('')
   await call.message.edit_text("Укажите время в данном формате ЧЧ ММ (например, 11 20):")


@rout.message(Newtask.time)
async def time(mes: Message, state: FSMContext):
    user_input = mes.text.strip()
    parts = user_input.split()
    
    if len(parts) != 2:
      await mes.answer("Неверный формат. Пожалуйста, введите время в формате ЧЧ ММ (например, 11 20):")
      return
    
    if len(parts[0]) != 2 or len(parts[1]) != 2:
      await mes.answer("Неверный формат. Пожалуйста, введите время в формате ЧЧ ММ (например, 11 20):")
      return


    try:
     hours = int(parts[0])
     minutes = int(parts[1])
    except ValueError:
     await mes.answer("Часы и минуты должны быть числами. Пожалуйста, введите время в формате ЧЧ ММ:")
     return 


    if not (0 <= hours <= 23 and 0 <= minutes <= 59):
      await mes.answer("Некорректное время. Часы должны быть от 00 до 23, минуты от 00 до 59. Попробуйте еще раз в формате ЧЧ ММ:")
      return 

    await state.update_data(time_s=f"{hours:02d}:{minutes:02d}")
    user_data = await state.get_data()
    task = user_data.get("task_s", "Задача не указана")
    month = user_data.get("month_s", "Месяц не выбран") 
    time = user_data.get("time_s", "Время не указано")
    await mes.answer(f"Итак, твое напоминание: {task} на {month}? День {time}. Все верно?")


