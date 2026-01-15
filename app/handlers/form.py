from aiogram import Router, Bot

from app.states import VideoFlow
from app.handlers.video import video_data
from app.keyboards.inline import next_video_kb

from app.database import add_user
from app.config import SYSTEM_BOT_TOKEN, ADMIN_ID


router = Router()


system_bot = Bot(token=SYSTEM_BOT_TOKEN)

@router.message()
async def user_phone_handler(message, state):
    if message.contact:
        phone = message.contact.phone_number
        first_name = message.contact.first_name or ""
        last_name = message.contact.last_name or ""
        name = f"{first_name} {last_name}".strip()

        is_new_user = await add_user(name=name, phone=phone)
        if is_new_user:
            notification = (
                f"<b>New User Registered!</b>\n"
                f"<b>Name:</b> {name}\n"
                f"<b>Phone:</b> <code>{phone}</code>"
            )

            try:
                await system_bot.send_message(chat_id=ADMIN_ID, text=notification, parse_mode="HTML")
            except Exception as e:
                print(f"Cannot send notification: {e}")
        else:
            print("User already exists")

        await state.update_data(phone=phone, name=name)
        await message.answer("Vă mulţumim, acum putem continua")

        await state.set_state(VideoFlow.watching_videos)
        await state.update_data(video_index=0)

        first_video = video_data[0]

        await message.answer_video(
            video=first_video["id"],
            caption=first_video["caption"],
            reply_markup=next_video_kb()
        )

    else:
        await message.answer("Vă rugăm să apăsați butonul pentru a partaja numărul")
