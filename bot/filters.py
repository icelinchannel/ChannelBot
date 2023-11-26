from aiogram.filters.base import Filter

from aiogram import F

from config import CHANNEL_ID, GROUP_ID

class GroupRouterFilter(Filter):
    def __call__(self):
        return F.chat.id == GROUP_ID
