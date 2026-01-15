import asyncio
import logging

from aiogram import F, Bot, Dispatcher

from app.config import SYSTEM_BOT_TOKEN, ADMIN_ID
from app.database import get_all_users, User, init_db
from app.keyboards.reply import admin_kb

logging.basicConfig(level=logging.INFO)

bot = Bot(token=SYSTEM_BOT_TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def admin_start(message):
    if str(message.from_user.id) == str(ADMIN_ID):
        await message.answer("Welcome to admin panel!", reply_markup=admin_kb())
    else:
        await message.answer("Access denied")


@dp.message(F.text == "ShowAllUsers")
async def show_all_users_command(message):
    if str(message.from_user.id) != str(ADMIN_ID):
        return
    users = await get_all_users()
    if not users:
        await message.answer("No data for now")
        return
    response = "📋 <b>Users List:</b>\n"
    response += "━━━━━━━━━━━━━━━━━━━━\n"
    for user in users:
        response += f"👤 {user.name} — <code>{user.phone}</code>\n"

    await message.answer(response, parse_mode="HTML")

async def main():
    await  init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())






