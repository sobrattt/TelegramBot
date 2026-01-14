from aiogram.types import Message
from aiogram import Router
from aiogram.fsm.context import FSMContext

from app.states import VideoFlow
from app.handlers.video import videos
from app.keyboards.inline import next_video_kb

router = Router()

@router.message()
async def user_phone_handler(message, state):
    if message.contact:
        phone = message.contact.phone_number
        first_name = message.contact.first_name or ""
        last_name = message.contact.last_name or ""
        name = f"{first_name}{last_name}".strip()
        await state.update_data(phone=phone, name=name)
        await message.answer("Vă mulţumim, acum putem continua")

        await state.set_state(VideoFlow.watching_videos)
        await state.update_data(video_index=0)

        first_video_id = videos[0]

        await message.answer_video(
            video=first_video_id,
            reply_markup=next_video_kb()
        )

    else:
        await message.answer("Vă rugăm să apăsați butonul pentru a partaja numărul")
