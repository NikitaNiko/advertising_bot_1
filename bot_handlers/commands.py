from aiogram import Router
from bot_keyboards.inline_kb import inline_kb, inline_kb_check_pay
from aiogram.types import Message
from aiogram.filters import CommandStart
from bot_database.db import get_reg


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    flag = await get_reg(message.from_user.id)
    if (flag == 2):
        await message.answer_photo("AgACAgIAAxkBAAINvWVPNHe_8zTvi66DSlD4PgQ_jOMGAAKQzDEbtbt4So4l083sSm2lAQADAgADeQADMwQ", caption="""✅РЕГИСТРАЦИЯ УСПЕШНА!\n\n
⚠️Для того, чтобы получить доступ в ВИП чат к сигналам и Нашему Софту, необходимо пополнить баланс на сумму 1000 RUB (10$) с аккаунта который вы только, зарегистрировали.\n\n
✅После первого пополнения нажмите на кнопку ПРОВЕРИТЬ ПОПОЛНЕНИЯ\n\n
👨‍💻Если у вас есть вопросы, напиши мне""", reply_markup=inline_kb_check_pay)
    else:
        await message.answer_video("BAACAgIAAxkBAAINeWVOjGnbmvHX3SbgHqNPjJH6pE0BAAIWPwACqthwSoqEhMQH-0g1MwQ", caption="""‼Обязательно перед началом посмотри видео👆                  
🔥Привет, меня зовут Саша, и я зарабатываю на своем софте по взлому Lucky Jet и Rocket Queen, в видео я показал, как это работает!
💰Хочешь зарабатывать как я? 
📍Если возникли вопросы пиши мне в любое время по кнопке "Написать мне"
""", reply_markup=inline_kb)