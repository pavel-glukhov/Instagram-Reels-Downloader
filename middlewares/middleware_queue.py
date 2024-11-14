from aiogram import BaseMiddleware
from typing import Callable, Dict, Any
from aiogram.types import Message

class QueueMiddleware(BaseMiddleware):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    async def __call__(self, handler: Callable, event: Message, data: Dict[str, Any]) -> Any:
        data["queue"] = self.queue
        return await handler(event, data)