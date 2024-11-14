import asyncio
import logging
import os
import aiohttp
from aiogram.types import FSInputFile
from instagram_reels.main.InstagramAPIClientImpl import InstagramAPIClientImpl

logger = logging.getLogger(__name__)

async def init_client():
    try:
        client = await InstagramAPIClientImpl().reels()
        return client
    except Exception as e:
        logger.error(f"Client initialization error: {e}")
        return None

async def download_reels(clip_name: str, reel_id: str, client):
    if not client:
        logger.error("Client initialization failed. Exiting download process.")
        return None
    try:
        info = await client.get(reel_id)
        if not info.videos:
            logger.error("No videos found for the provided reel ID.")
            return None

        async with aiohttp.ClientSession() as session:
            async with session.get(info.videos[0].url) as response:
                if response.status == 200:
                    with open(clip_name, "wb+") as out_file:
                        out_file.write(await response.read())
                    logger.info(f"Video {clip_name} successfully downloaded.")
                    return clip_name
                else:
                    logger.error(f"Failed to download video: {response.status}")
                    return None
    except aiohttp.ClientError as e:
        logger.error(f"Video download error: {e}")
        return None
    except IOError as e:
        logger.error(f"File saving error: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error during video download: {e}")
        return None

async def process_queue(client, queue):
    while True:
        message, shortcode = await queue.get()
        try:
            file_name = await download_reels(f"temp_folder\\{shortcode}.mp4", shortcode, client)
            if file_name:
                video_file = FSInputFile(f"temp_folder\\{shortcode}.mp4")
                try:
                    await message.answer_video(video=video_file)
                    os.remove(file_name)
                    logger.info(f"Video {file_name} sent and deleted from local storage.")
                except Exception as e:
                    logger.error(f"Error sending video: {e}")
                    await message.answer('Error sending the video.')
            else:
                await message.answer('Error downloading the video.')
                logger.error("Failed to download the video.")
        except Exception as e:
            await message.answer(f"Unexpected error occurred: {e}")
            logger.error(f"Unexpected error during queue processing: {e}")
        finally:
            queue.task_done()