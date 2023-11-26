from aiogram.filters.base import Filter

from aiogram.enums.chat_type import ChatType
from aiogram import F

from config import CHANNEL_ID, GROUP_ID

class GroupRouterFilter(Filter):
    def __call__(self):
        return F.chat.id == GROUP_ID

class ChannelRouterFilter(Filter):
    def __call__(self):
        return F.chat.id == CHANNEL_ID


class PrivateRouterFilter(Filter):
    def __call__(self):
        return F.chat.type == ChatType.PRIVATE
