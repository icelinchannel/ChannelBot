from aiogram import F

from aiogram.filters.command import Command
from aiogram.enums.chat_type import ChatType

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

import asyncio

from config import bot, dp, private_rt, group_rt, channel_rt, CHANNEL_ID, GROUP_ID
from handlers import welcome, bot_added_to_another_group, start
from filters import IsItThisBotFilter, PrivateRouterFilter, GroupRouterFilter, ChannelRouterFilter


private_rt.message.filter(PrivateRouterFilter())
group_rt.message.filter(GroupRouterFilter())
channel_rt.message.filter(ChannelRouterFilter())

private_rt.channel_post.filter(PrivateRouterFilter())
group_rt.channel_post.filter(GroupRouterFilter())
channel_rt.channel_post.filter(ChannelRouterFilter())

private_rt.chat_member.filter(PrivateRouterFilter())
group_rt.chat_member.filter(GroupRouterFilter())
channel_rt.chat_member.filter(ChannelRouterFilter())

dp.include_routers(group_rt, private_rt, channel_rt)


group_rt.chat_member.register(welcome, ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
