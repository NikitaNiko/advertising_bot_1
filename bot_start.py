from aiogram import Bot, Dispatcher
import asyncio
from bot_handlers import commands, states, request_to_join, messages


bot = Bot("5647971616:AAEUmfKipJ7t2rk-tbIHcYHGfZWNTyg5WaM")

async def main():
    
    dp = Dispatcher()
    
    dp.include_routers (
        commands.router,
        request_to_join.router,
        messages.router,
        states.router,
    )
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

    

if __name__ == "__main__":
    asyncio.run(main())