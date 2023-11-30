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

    async def __init__(self, user_id):
        self.user_id = user_id

    async def __call__(self):
        member = await bot.get_chat_member(chat_id=CHANNEL_ID, user_id=self.user_id)
        return member.is_member


class IsItBotFilter(Filter):
    async def __call__(self, event: types.ChatMemberUpdated):
        return event.new_chat_member.user.id == bot.id
