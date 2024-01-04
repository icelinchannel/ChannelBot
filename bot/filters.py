from aiogram import F, types

from aiogram.filters.base import Filter
from aiogram.enums.chat_type import ChatType

import logging
import sys

from config import CHANNEL_ID, GROUP_ID, bot


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
       '%(lineno)d - %(name)s - %(message)s',
    style='{',
    filename='logs/main.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

stderr_handler = logging.StreamHandler()
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)


class GroupRouterFilter(Filter):
    async def __call__(self, message):
        return F.chat_id == GROUP_ID


class ChannelRouterFilter(Filter):
    async def __call__(self, message):
        return F.chat_id == CHANNEL_ID


class PrivateRouterFilter(Filter):
    async def __call__(self, message):
        return F.chat_type == ChatType.PRIVATE


class IsItThisBotFilter(Filter):
    async def __call__(self, event: types.ChatMemberUpdated):
        return event.new_chat_member.user.id == bot.id
