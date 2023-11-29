from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

class Pagination(CallbackData, prefix="page"):
    action: str


inline_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💰 Получить софт", callback_data=Pagination(action="yes").pack()),

        ],
        [
            InlineKeyboardButton(text="👩‍💻 Написать мне", url="https://t.me/pricklyman0"),
        ],
        [
            InlineKeyboardButton(text="🔥 Перейти в канал", url="https://t.me/+qplCohkkYbw4NTU6"),
        ],
    ],
    resize_keyboard=True,
)

inline_kb_sub = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="🔥 Перейти в канал", url="https://t.me/+qplCohkkYbw4NTU6"),
        ],
    ],
    resize_keyboard=True,
)

inline_kb_check_pay = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💸ПОПОЛНИТЬ", url="https://raujet.com/deposit?id=318592"),
        ],
        [
            InlineKeyboardButton(text="🔍ПРОВЕРИТЬ ПОПОЛНЕНИЕ", callback_data=Pagination(action="no").pack()),
        ],
        [
            InlineKeyboardButton(text="👩‍💻 Написать мне", url="https://t.me/pricklyman0"),
        ],
    ],
    resize_keyboard=True,
)

inline_kb_reg = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="📲РЕГИСТРАЦИЯ", url="https://raujet.com/deposit?id=318592"),
        ],
        [
            InlineKeyboardButton(text="🔍ПРОВЕРИТЬ РЕГИСТРАЦИЮ", callback_data=Pagination(action="no").pack()),
        ],
        [
            InlineKeyboardButton(text="👩‍💻 Написать мне", url="https://t.me/pricklyman0"),
        ],
    ],
    resize_keyboard=True,
)
    
    

    

