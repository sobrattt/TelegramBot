import asyncio
import logging
from app.bot import bot,dp

from app.handlers.start import router as start_router
from app.handlers.form import router as form_router
from app.handlers.video import router as video_router

from app.database import init_db
logging.basicConfig(level=logging.INFO)

async def main():
    await init_db()

    dp.include_router(start_router)
    dp.include_router(form_router)
    dp.include_router(video_router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    asyncio.run(main())