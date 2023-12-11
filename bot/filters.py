from aiogram import F, types

from aiogram.filters.base import Filter
from aiogram.enums.chat_type import ChatType

from config import CHANNEL_ID, GROUP_ID, bot


class GroupRouterFilter(Filter):
    async def __call__(self, message):
        return F.chat.id == GROUP_ID


class ChannelRouterFilter(Filter):
    async def __call__(self, message):
        return F.chat.id == CHANNEL_ID


class PrivateRouterFilter(Filter):
    async def __call__(self, message):
        return F.chat.type == ChatType.PRIVATE


class IsItThisBotFilter(Filter):
    async def __call__(self, event: types.ChatMemberUpdated):
        return event.new_chat_member.user.id == bot.id
