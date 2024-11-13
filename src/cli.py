import os
import asyncio

from aiogram import Bot, Dispatcher

from src.downloader.client import init_client, process_queue
from src.handlers import downloads
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init_routers(dp):
    dp.include_router(downloads.router)

async def run_app():
    bot = Bot(token=os.getenv('API_TOKEN'))
    dp = Dispatcher()
    init_routers(dp)
    client = await init_client()
    if client is None:
        logger.error("Failed to initialize Instagram client.")
        return

    if not os.path.exists('temp_folder'):
        os.makedirs('temp_folder')
    asyncio.create_task(process_queue(client))

    try:
        await dp.start_polling(bot, close_bot_session=True)
    except KeyboardInterrupt:
        logger.info("Program terminated by user (KeyboardInterrupt).")
    except asyncio.TimeoutError as e:
        logger.error(f"Timeout error occurred: {e}")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")

if __name__ == '__main__':
    asyncio.run(run_app())
