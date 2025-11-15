from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext 


class Newtask(StatesGroup):
    name_task = State()
    month = State()
    time = State()