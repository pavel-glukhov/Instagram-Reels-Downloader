import re

from aiogram.filters import Command
from aiogram import types, Router
import logging

from src.downloader.client import queue

router = Router()
logger = logging.getLogger(__name__)


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Send here a link to download reels from Instagram.')


@router.message()
async def check_link(message: types.Message):
    url_pattern = r"https?://(www\.)?instagram\.com/(reel|reels)/([^/?#&]+)"
    match = re.search(url_pattern, message.text)
    if match:
        await message.answer('Added to download queue.')
        await queue.put((message, match.group(3)))
    else:
        await message.answer('Invalid link.')
        logger.warning("User provided an invalid link.")
