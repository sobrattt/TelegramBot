from aiogram.filters import Command
from aiogram.types import Message
from app.keyboards.reply import user_phone_info_keyboard
from aiogram import Router

router = Router()

@router.message(Command("start"))
async def start_handler(message: Message):
    text = (
        "Bine ai venit! 👋\n"
        "Acest canal este pentru antreprenori, freelanceri și profesioniști "
        "care câștigă deja bani, dar simt că există un prag invizibil peste care nu trec.\n\n"
        "Aici NU vei găsi:\n"
        "– motivație\n"
        "– tehnici rapide\n"
        "– promisiuni goale\n\n"
        "Vei găsi:\n"
        "– explicații clare despre blocajele subconștiente\n"
        "– de ce munca și strategiile nu mai dau rezultate\n"
        "– cum starea interioară influențează direct banii și deciziile\n\n"
        "▶️ Urmărește video-urile în ordine.\n"
        "Fiecare continuă exact de unde se oprește cel anterior.\n"
        "Dacă ceva rezonează, vei ști singur ce urmează.\n\n"
        "Apăsați butonul de mai jos pentru a continua 👇"
    )

    await message.answer(text, reply_markup=user_phone_info_keyboard)