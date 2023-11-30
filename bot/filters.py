from aiogram.filters.base import Filter

from aiogram.enums.chat_type import ChatType
from aiogram import F

from config import CHANNEL_ID, GROUP_ID, bot


class GroupRouterFilter(Filter):
    async def __call__(self, message):
        return F.chat.id == GROUP_ID


class ChannelRouterFilter(Filter):
    async def __call__(self, message):
        return F.chat.id == CHANNEL_ID


class IsItBotFilter(Filter):
    async def __call__(self, event):
        bot_obj = await bot.get_me()
        bot_id = bot_obj.id

        for chat_member in event.new_chat_members:
            if chat_member.id == bot_id:
                return True
        return F.chat.type == ChatType.SUPERGROUP
