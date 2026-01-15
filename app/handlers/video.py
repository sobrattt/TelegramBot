from aiogram import Router, F

from app.states import VideoFlow
from app.config import VIDEO_1, VIDEO_2, VIDEO_3, VIDEO_4
from app.keyboards.inline import next_video_kb, final_kb

router = Router()

video_data = [
    {
        "id": VIDEO_1,
        "caption": (
            "De ce majoritatea antreprenorilor muncesc mult, învață constant\n"
            "și totuși rămân sub potențialul lor real.\n"
            "Acest video pune baza pentru tot ce urmează.\n"
            "Urmărește-l până la capăt."
        )
    },
    {
        "id":VIDEO_2,
        "caption": (
            "Dacă ai recunoscut ceva din tine în acest video, este normal.\n"
            "Problema NU este lipsa de disciplină sau de inteligență.\n"
            "Există un mecanism mai profund care se activează exact când apare creșterea.\n"
            "▶️ Video 2 explică de ce, pentru mulți oameni, banii pot deveni „pericol” la nivel subconștient"
        )
    },
    {
        "id": VIDEO_3,
        "caption": (
            "Dacă acest video a atins un punct sensibil, este un semn bun.\n"
            "Multe dintre aceste programe nu sunt create de tine,\n"
            "ci preluate din familie, copilărie sau contexte vechi.\n"
            "▶️ Video 3 vorbim despre emoțiile primare care mențin aceste blocaje active."
        )
    },
    {
        "id": VIDEO_4,
        "caption": (
            "▶️ Video 4 explică de ce starea interioară este factorul principal și ce se schimbă atunci când blocajele sunt eliminate."
        )
    }
]

@router.callback_query(
    VideoFlow.watching_videos,
    F.data == "next_video"
)
async def next_video(callback, state):
    data = await state.get_data()
    video_index = data.get("video_index", 0)
    video_index += 1
    if video_index < len(video_data):
        await state.update_data(video_index=video_index)
        current_video = video_data[video_index]
        await callback.message.answer_video(
            video=current_video["id"],
            caption=current_video["caption"],
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


