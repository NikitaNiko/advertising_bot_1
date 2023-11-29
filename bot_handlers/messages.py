from aiogram import Router, F
from aiogram.types import CallbackQuery
from bot_keyboards import inline_kb

router = Router()

@router.callback_query(inline_kb.Pagination.filter(F.action == "yes"))
async def pagination_handler(call: CallbackQuery, callback_data: inline_kb.Pagination):
    await call.bot.send_photo(chat_id=call.from_user.id, photo="AgACAgIAAxkBAAIN92VPQXXrS7r2QfXCGtT4ZwF_EWPDAALVzDEbtbt4SiU-VX3ykF0UAQADAgADeQADMwQ", caption="""Привет!🔥 Если ты хочешь зарабатывать по БОЛЬШИМ КОЭФФИЦИЕНТАМ и пользоваться НАШИМ ЛИЧНЫМ ВЗЛОМ СОФТОМ с коэффициентами 4-6x в нашем закрытом ВИП чате\n\n
⚠️Нужно выполнить ряд действий для того что бы Стратегия начала работать!\n\n 
✅ЭТО БЕСПЛАТНО✅\n\n
❌Без этих действий стратегия работать не будет❌\n\n
📲Для начала необходимо провести регистрацию на сайте игры LuckyJet.\n\n
1. 📍Аккаунт должен быть НОВЫМ, если вы переходите по ссылке и попадаете на старый, необходимо выйти с него и заново перейти по кнопке «РЕГИСТРАЦИЯ»\n\n
2. 📍После РЕГИСТРАЦИИ, нажмите кнопку «ПРОВЕРИТЬ РЕГИСТРАЦИЮ»\n\n
👨‍💻Если у вас есть вопросы, напиши мне 
""", reply_markup=inline_kb.inline_kb_reg)

    await call.answer()

@router.callback_query(inline_kb.Pagination.filter())
async def pagination_handler(call: CallbackQuery, callback_data: inline_kb.Pagination):
    await call.answer("123")
    await call.bot.send_message(chat_id=call.from_user.id, text="123")
