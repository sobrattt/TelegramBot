from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def next_video_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="▶️Următorul videoclip",
                    callback_data = "next_video"
                )
            ]
        ]
    )

def final_kb():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="Programați-vă pentru o consultație", url="https://t.me/vasilcicdragomir")],
            [InlineKeyboardButton(text="Accesați canalul principal", url="https://t.me/+MN90jt7rvwhjNmQy")]
        ]
    )