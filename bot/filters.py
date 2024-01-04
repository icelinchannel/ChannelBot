from aiogram import F, types

from aiogram.filters.base import Filter
from aiogram.enums.chat_type import ChatType

import logging
import sys

from config import CHANNEL_ID, GROUP_ID, bot


logging.basicConfig(
    level=logging.DEBUG,
    format='''[%(asctime)s] #%(levelname)-8s %(filename)s:
%(lineno)d - %(name)s - %(message)s''',
    filename=f'logs/{__name__}.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)


class GroupRouterFilter(Filter):
    async def __call__(self, message):
        logger.info('GroupRouterFilter was used')
        return F.chat_id == GROUP_ID


class ChannelRouterFilter(Filter):
    async def __call__(self, message):
        logger.info('GroupRouterFilter is used')
        return F.chat_id == CHANNEL_ID


class PrivateRouterFilter(Filter):
    async def __call__(self, message):
        logger.info('PrivateRouterFilter is used')
        return F.chat_type == ChatType.PRIVATE


class IsItThisBotFilter(Filter):
    async def __call__(self, event: types.ChatMemberUpdated):
        logger.info('IsItThisBotFilter is used')
        return event.new_chat_member.user.id == bot.id
