from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram import Router, F
from aiogram.fsm.context import FSMContext 
from app.state import Newtask, Edittask
from config import bot, dp, scheduler
from aiogram import Bot, Dispatcher
from app import keyb as kb
import logging
from datetime import datetime, timedelta
from apscheduler.triggers.date import DateTrigger
import pytz 

rout = Router()

bt = bot

 

day_names_map = {
  "day_One": 1,"day_Two": 2,"day_Three": 3,"day_Four": 4,"day_Five": 5,
  "day_Six": 6,"day_Seven": 7,"day_Eight": 8,"day_Nine": 9,"day_Ten": 10,"day_Eleven": 11,
  "day_Twelve": 12,"day_Thirteen": 13,"day_Fourteen": 14,"day_Fifteen": 15,"day_Sixteen": 16,
  "day_Seventeen": 17,"day_Eighteen": 18,"day_Nineteen": 19,"day_Twenty": 20,"day_Twenty-one": 21,
  "day_Twenty-two": 22,"day_Twenty-three": 23,"day_Twenty-four": 24,"day_Twenty-five": 25,"day_Twenty-six": 26,
  "day_Twenty-seven": 27,"day_Twenty-eight": 28,"day_Twenty-nine": 29,"day_Thirty": 30,"day_Thirty-one": 31
}



@rout.message(CommandStart())
async def cmd_start(mes: Message):     
    logging.info(f"Получена команда /start от пользователя {mes.from_user.id}")
    logging.info(f"Планировщик запущен")
    user_name = mes.from_user.full_name
    await mes.answer_photo(photo="AgACAgIAAxkBAAIDH2k0hJohau-7BodO9yYYUJMJOPceAAIaC2sbB3OpSZW7JICWV0j3AQADAgADeQADNgQ",
                           caption=f"Привет, {user_name}! Я помогу тебе записать самое важное и напомню обо всем, что нужно 😌 \nЖмакай на новое напоминание", reply_markup=kb.main)
   



#выбор часового пояса/проверка 
@rout.callback_query(F.data == "newtask")
async def new_task(call:CallbackQuery, state: FSMContext):
    await state.set_state(Newtask.utc)
    await call.answer()
    await call.bot.send_message(
  chat_id=call.from_user.id, # Или call.message.chat.id
  text='Выбери часовой пояс', reply_markup=kb.utc
)



@rout.callback_query(Newtask.utc, F.data.startswith("utc_"))
async def month(call: CallbackQuery, state: FSMContext): 
   callback_data_utc = call.data
   print(callback_data_utc)
   print(callback_data_utc[4:])
   

   month_names_utc = {
    "utc_Europe/Kaliningrad": "Калининград", "utc_Europe/Moscow": "Москва", "utc_Europe/Samara": "Самара", "utc_Asia/Yekaterinburg": "Екатеринбург",
    "utc_Asia/Omsk": "Омск", "utc_Asia/Krasnoyarsk": "Красноярск", "utc_Asia/Irkutsk": "Иркутск", "utc_Asia/Chita": "Чита",
    "utc_Asia/Vladivostok": "Владивосток", "utc_Asia/Sakhalin": "Сахалин", "utc_Asia/Kamchatka": "Камчатка"
 }
   targ = month_names_utc[callback_data_utc]
   print(targ)
   await state.update_data(utc_s=callback_data_utc[4:])
   await state.set_state(Newtask.name_task)
   await call.answer('')
   await call.message.edit_text('О чем тебе напомнить? Напиши кратко так, как было понятно тебе 💚')




@rout.message(F.photo)
async def get_photo_id(message: Message):
 photo_file_id = message.photo[-1].file_id
 print(photo_file_id)



@rout.message(Command("help"))
async def help(mes: Message):
    logging.info(f"Получена команда /help от пользователя {mes.from_user.id}")
    await mes.answer('Help')



#создание новых задач
#установка новой задачи
@rout.message(Newtask.name_task)
async def name_task(mes: Message, state: FSMContext):
    await state.update_data(task_s=mes.text)
    await state.set_state(Newtask.month)
    await mes.answer("ВыберИИИИИ , в какой месяц напомнить", reply_markup=kb.month)


#выбор месяца
@rout.callback_query(Newtask.month, F.data.startswith("month_"))
async def month(call: CallbackQuery, state: FSMContext): 
   callback_data_month = call.data 
   print(callback_data_month)
   month_names_map = {
    "month_one": "Январь", "month_two": "Февраль", "month_three": "Март", "month_four": "Апрель",
    "month_five": "Май", "month_six": "Июнь", "month_seven": "Июль", "month_eight": "Август",
    "month_nine": "Сентябрь", "month_ten": "Октябрь", "month_eleven": "Ноябрь", "month_twelve": "Декабрь"
 }
   targ = month_names_map[callback_data_month]
   global num;
   targ_31 = ["Январь","Март","Май","Июль","Август","Октябрь","Декабрь"]
   targ_30 = ["Апрель","Июнь","Сентябрь","Ноябрь"]

   if targ == "Февраль":
      num = kb.number_28
   
   if targ in targ_30:
      num = kb.number_30

   if targ in targ_31:
      num = kb.number_31

   display_month_name = month_names_map[callback_data_month]
   await state.update_data(month_s=display_month_name)
   await state.set_state(Newtask.day)
   await call.answer('')
   await call.message.edit_text("Укажите в какой день вам напомнить: ", reply_markup=num)


#выбор дня
@rout.callback_query(Newtask.day, F.data.startswith("day_"),F.data.in_(day_names_map))
async def month(call: CallbackQuery, state: FSMContext): 
   callback_data_day = call.data 
   print(callback_data_day)
   print(day_names_map[callback_data_day])
   display_day_name = day_names_map[callback_data_day]
   await state.update_data(day_s=display_day_name)
   await state.set_state(Newtask.time)
   await call.answer('')
   await call.message.edit_text("Укажите время в данном формате ЧЧ ММ (например, 11 20):")


async def send_scheduled_message_job(mesbot, chat_id: int, message_text: str):
  print(f"Ваша задача отправлена - {message_text}")
  await mesbot.send_message(chat_id, message_text)


#выбор времени
@rout.message(Newtask.time)
async def time(mes: Message, state: FSMContext):
    target_chat_id = mes.chat.id
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
#вывод задачи
    hour = parts[0]
    minut = parts[1]
    await state.update_data(time_s=f"{hours:02d}:{minutes:02d}")
    user_data = await state.get_data()
    task = user_data.get("task_s", "Задача не указана")
    month = user_data.get("month_s", "Месяц не выбран") 
    day = user_data.get("day_s", "День не указан")
    time = user_data.get("time_s", "Время не указано")
    utc = user_data.get("utc_s", "Время не указано")
    message_text = task
    user_tz = pytz.timezone(utc)
    current_time_in_tz = datetime.now(user_tz)
    scheduled_time = current_time_in_tz + timedelta(seconds=10)
    scheduler.add_job(                     #добавление задачи в планировщик
        send_scheduled_message_job,       # Функция, которую нужно выполнить
        DateTrigger(run_date=scheduled_time.astimezone(pytz.utc)), # Когда выполнить (точный datetime)
        args=[mes.bot, target_chat_id, message_text], # Аргументы для нашей функции
        id="simple_message_job",             # Уникальный ID для этой задачи
    )
    print("Задача запланирована")
   #  await mes.answer(f"Итак, твое напоминание: {task} на {month}? День {day} в {time}. Все верно?", reply_markup=kb.check)
 




#-------------------------------------------------------------редактирование

@rout.callback_query(F.data == "No_0")
async def NO(call:CallbackQuery):
  await call.answer()
  await call.message.edit_text(text = "Что вы хотите изменить?",  reply_markup=kb.task)


#редактирование задачи 
@rout.callback_query(F.data == "text")
async def new_task(call:CallbackQuery, state: FSMContext):
    await state.set_state(Edittask.edit_name_task)
    await call.answer()
    await call.bot.send_message(
  chat_id=call.from_user.id, # Или call.message.chat.id
  text='Напиши новое напоминание:'
)

#редактирование задачи
@rout.message(Edittask.edit_name_task)
async def month(mes: Message, state: FSMContext): 
   await state.update_data(task_s=mes.text)
   user_data = await state.get_data()
   task = user_data.get("task_s", "Задача не указана")
   month = user_data.get("month_s", "Месяц не выбран") 
   day = user_data.get("day_s", "День не указан")
   time = user_data.get("time_s", "Время не указано")
   await mes.answer(f"Итак, твое напоминание: {task} на {month}? День {day} в {time}. Все верно?", reply_markup=kb.check)


@rout.callback_query(F.data == "m")
async def new_task(call:CallbackQuery, state: FSMContext):
    await state.set_state(Edittask.edit_month)
    await call.answer()
    await call.bot.send_message(
  chat_id=call.from_user.id, # Или call.message.chat.id
  text='Выбери новый месяц:', reply_markup=kb.month)
    

#редактирование месяца
@rout.callback_query(Edittask.edit_month)
async def month(call: CallbackQuery, state: FSMContext): 
   callback_data_month = call.data 
   print(callback_data_month)
   month_names_map = {
    "month_one": "Январь", "month_two": "Февраль", "month_three": "Март", "month_four": "Апрель",
    "month_five": "Май", "month_six": "Июнь", "month_seven": "Июль", "month_eight": "Август",
    "month_nine": "Сентябрь", "month_ten": "Октябрь", "month_eleven": "Ноябрь", "month_twelve": "Декабрь"
 }
   targ = month_names_map[callback_data_month]
   global num;
   targ_31 = ["Январь","Март","Май","Июль","Август","Октябрь","Декабрь"]
   targ_30 = ["Апрель","Июнь","Сентябрь","Ноябрь"]

   if targ == "Февраль":
      num = kb.number_28
   
   if targ in targ_30:
      num = kb.number_30

   if targ in targ_31:
      num = kb.number_31

   display_month_name = month_names_map[callback_data_month]
   await state.update_data(month_s=display_month_name)
   await state.set_state(Edittask.edit_day)
   await call.answer('')
   await call.bot.send_message(
   chat_id=call.from_user.id, # Или call.message.chat.id
   text='Выберите новое число:', reply_markup=num)


#редактирование дня
@rout.callback_query(F.data == "nir")
async def month(call: CallbackQuery, state: FSMContext): 
   await state.set_state(Edittask.edit_day)
   await call.answer('')
   await call.bot.send_message(
   chat_id=call.from_user.id, # Или call.message.chat.id
   text='Выберите новое число:', reply_markup=num)


@rout.callback_query(Edittask.edit_day, F.data.in_(day_names_map))
async def month(call: CallbackQuery, state: FSMContext): 
  callback_data_day = call.data 
  print(callback_data_day)
  display_day_name = day_names_map[callback_data_day]
  await state.update_data(day_s=display_day_name)
  user_data = await state.get_data()
  task = user_data.get("task_s", "Задача не указана")
  month = user_data.get("month_s", "Месяц не выбран") 
  day = user_data.get("day_s", "День не указан")
  time = user_data.get("time_s", "Время не указано")
  await call.bot.send_message(chat_id=call.message.chat.id, text=f"Итак, твое напоминание: {task} на {month}? День {day} в {time}. Все верно?", reply_markup=kb.check)



#редактирование времени
@rout.callback_query(F.data == "tir")
async def new_task(call:CallbackQuery, state: FSMContext):
    await state.set_state(Edittask.edit_time)
    await call.answer()
    await call.bot.send_message(
    chat_id=call.from_user.id, # Или call.message.chat.id
    text='Укажите новое время в формате ЧЧ ММ (например, 11 20):')


@rout.message(Edittask.edit_time)
async def month(mes: Message, state: FSMContext): 
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
#вывод задачи
  await state.update_data(time_s=f"{hours:02d}:{minutes:02d}")
  user_data = await state.get_data()
  task = user_data.get("task_s", "Задача не указана")
  month = user_data.get("month_s", "Месяц не выбран") 
  day = user_data.get("day_s", "День не указан")
  time = user_data.get("time_s", "Время не указано")
  await mes.answer(f"Итак, твое напоминание: {task} на {month}? День {day} в {time}. Все верно?", reply_markup=kb.check)



@rout.callback_query(F.data == "Yes_1")
async def NO(call:CallbackQuery):
  await call.answer()
  await call.message.edit_text(text = "Напоминание успешно создано")
