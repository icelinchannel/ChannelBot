from aiogram import F

from aiogram.filters.command import Command
from aiogram.enums.chat_type import ChatType

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

import asyncio
import logging
import sys

from config import bot, dp, private_rt, group_rt, channel_rt, owner_rt, GROUP_ID, CHANNEL_ID, OWNER_ID
from handlers import welcome, start_private, start_group, copy
from filters import OwnerRouterFilter, PrivateRouterFilter, GroupRouterFilter, ChannelRouterFilter, IsItThisBotFilter


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


private_rt.message.filter(PrivateRouterFilter())
group_rt.message.filter(GroupRouterFilter())
channel_rt.message.filter(ChannelRouterFilter())
owner_rt.message.filter(OwnerRouterFilter())

private_rt.chat_member.filter(PrivateRouterFilter())
group_rt.chat_member.filter(GroupRouterFilter())
channel_rt.chat_member.filter(ChannelRouterFilter())
owner_rt.chat_member.filter(OwnerRouterFilter())

dp.include_routers(group_rt, private_rt, channel_rt, owner_rt)


group_rt.chat_member.register(welcome, ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
group_rt.message.register(start_group, Command('start'))
private_rt.message.register(start_private, Command('start'))
private_rt.message.register(copy)
private_rt.edited_message.register(copy)


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
