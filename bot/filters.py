from aiogram import types

from aiogram.filters.base import Filter
from aiogram.enums.chat_type import ChatType

import logging
import sys
from typing import Union

from config import bot, CHANNEL_ID, GROUP_ID, OWNER_ID


logging.basicConfig(
    level=logging.DEBUG,
    format='''[%(asctime)s] #%(levelname)-8s %(filename)s:
%(lineno)d - %(name)s - %(message)s''',
    filename='logs/filters.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)


class ChatTypeFilter(Filter):
    def __init__(self, chat_type: Union[str, list]) -> None:
        self.chat_type = chat_type
        logger.info('ChatTypeFilter was initialized')

    async def __call__(self, message: types.Message) -> bool:

        logger.info('ChatTypeFilter was used')

        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type


class PrivateRouterFilter(Filter):
    async def __call__(self, message) -> bool:
        logger.info('PrivateRouterFilter was used')
        return ChatTypeFilter(chat_type=[ChatType.PRIVATE]).__call__(message=message) and message.chat.id != OWNER_ID


class GroupRouterFilter(Filter):
    async def __call__(self, message) -> bool:
        logger.info('GroupRouterFilter was used')
        return message.chat.id == GROUP_ID


class ChannelRouterFilter(Filter):
    async def __call__(self, message) -> bool:
        logger.info('ChannelRouterFilter was used')
        return message.chat.id == CHANNEL_ID


class OwnerRouterFilter(Filter):
    async def __call__(self, message) -> bool:
        logger.info('OwnerRouterFilter was used')
        return message.chat.id == OWNER_ID


class IsItThisBotFilter(Filter):
    async def __call__(self, event: types.ChatMemberUpdated) -> bool:
        logger.info('IsItThisBotFilter was used')
        return event.new_chat_member.user.id == bot.id
