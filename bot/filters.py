from aiogram import F, types

from aiogram.filters.base import Filter
from aiogram.enums.chat_type import ChatType

import logging
import sys
from typing import Union

from config import CHANNEL_ID, GROUP_ID, bot


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
    def __init__(self, chat_type: Union[str, list]):
        self.chat_type = chat_type

    async def __call__(self, message: types.Message) -> bool:
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type


class IsItThisBotFilter(Filter):
    async def __call__(self, event: types.ChatMemberUpdated):
        logger.info('IsItThisBotFilter was used')
        return event.new_chat_member.user.id == bot.id
