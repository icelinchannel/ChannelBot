from aiogram import F, types

from aiogram.filters.command import Command
from aiogram.enums.chat_type import ChatType

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

import asyncio
import logging
import sys

from config import bot, dp, private_rt, group_rt, channel_rt, GROUP_ID, CHANNEL_ID
from handlers import welcome, start_private
from filters import ChatTypeFilter, IsItThisBotFilter


logging.basicConfig(
    level=logging.DEBUG,
    format='''[%(asctime)s] #%(levelname)-8s %(filename)s:
%(lineno)d - %(name)s - %(message)s''',
    filename='logs/main.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)


private_rt.message.filter(ChatTypeFilter(chat_type=[ChatType.PRIVATE]))
group_rt.message.filter(F.chat_id == GROUP_ID)
channel_rt.message.filter(F.chat_id == CHANNEL_ID)

private_rt.chat_member.filter(ChatTypeFilter(chat_type=[ChatType.PRIVATE]))
group_rt.chat_member.filter(F.chat_id == GROUP_ID)
channel_rt.chat_member.filter(F.chat_id == CHANNEL_ID)

dp.include_routers(group_rt, private_rt, channel_rt)


group_rt.chat_member.register(welcome, ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
private_rt.message.register(start_private, Command('start'))



async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
