from aiogram.fsm.state import StatesGroup, State

class Timezone(StatesGroup):
    UTC = State()

class Newtask(StatesGroup):
    utc = State()
    name_task = State()
    month = State()
    day = State()
    time = State()

class Edittask(StatesGroup):
    edit_utc = State()
    edit_name_task = State()
    edit_month = State()
    edit_day = State()
    edit_time = State()

