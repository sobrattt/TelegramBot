# import asyncio
# from aiogram import Bot, Dispatcher
# from aiogram.types import Message
#
#
#
#
# bot = Bot(token=TOKEN)
# dp = Dispatcher()
#
# @dp.message()
# async def catch_id(message: Message):
#     if message.video:
#         print("VIDEO FILE_ID:", message.video.file_id)
#
# async def main():
#     await dp.start_polling(bot)
#
# asyncio.run(main())