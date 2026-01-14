from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext

from app.states import VideoFlow
from app.config import VIDEO_1, VIDEO_2, VIDEO_3, VIDEO_4
from app.keyboards.inline import next_video_kb, final_kb

router = Router()

videos = [VIDEO_1, VIDEO_2, VIDEO_3, VIDEO_4]

@router.callback_query(
    VideoFlow.watching_videos,
    F.data == "next_video"
)
async def next_video(callback, state):
    data = await state.get_data()
    video_index = data.get("video_index", 0)
    video_index += 1
    if video_index < len(videos):
        await state.update_data(video_index=video_index)
        await callback.message.answer_video(
            video=videos[video_index],
            reply_markup=next_video_kb()
        )
    else:
        await state.clear()
        text = (
            "Dacă ai ajuns până aici, înseamnă că ceva a rezonat.\n"
                "Lucrul cu subconștientul NU este pentru toată lumea.\n"
                "Este pentru cei care sunt gata să se vadă sincer\n"
                "și să schimbe ceea ce îi limitează din interior.\n"
                "Dacă simți că este momentul să mergi mai departe,\n"
                "următorul pas este unul personal.\n"
                "👉 Scrie-mi în privat cu cuvântul CLARITATE\n"
                "și îți voi spune dacă și cum te pot ajuta."
        )
        await callback.message.answer(text=text, reply_markup=final_kb())

    await callback.answer()


