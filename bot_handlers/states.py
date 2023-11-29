from aiogram.fsm.state import StatesGroup, State

from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import Router, F

class Form(StatesGroup):
    photo = State()

router = Router()

@router.message()
async def echo(message: Message):
    # w = await bot.get_chat("@testwolha")
    # print(w)
    await message.answer("ok")
    try:
        print(message.from_user.id)
    except:
        pass
    try:
        print(message.video.file_id)
    except:
        pass
    try:
        print(message.photo[-1].file_id)
    except:
        pass
        


