from aiogram.types import ChatJoinRequest
from bot_keyboards.inline_kb import inline_kb_sub
from bot_start import bot
from aiogram import Router

router = Router()

@router.chat_join_request()
async def approve_request(chat_join: ChatJoinRequest):
    await bot.send_message(chat_id=chat_join.from_user.id, text="👋Здравствуйте, Ты только что подписался на канал RAU Стратегии, Ваша заявка одобрена!", reply_markup=inline_kb_sub)
    await chat_join.approve()