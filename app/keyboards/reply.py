from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_phone_info_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(
            text="📱 Partajează numărul de telefon",
            request_contact=True
        )]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

def admin_kb():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="ShowAllUsers")]
        ],
        resize_keyboard=True
    )