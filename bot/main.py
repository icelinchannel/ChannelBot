from aiogram import Bot, Dispatcher, F, Router, types

from aiogram.enums.chat_type import ChatType

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

import asyncio

from config import bot, dp, private_rt, group_rt, channel_rt, CHANNEL_ID, GROUP_ID
from handlers import welcome


private_rt.message.filter(F.chat.type == ChatType.PRIVATE)
group_rt.message.filter(F.chat.id == GROUP_ID)
channel_rt.message.filter(F.chat.id == CHANNEL_ID)

private_rt.channel_post.filter(F.chat.type == ChatType.PRIVATE)
group_rt.channel_post.filter(F.chat.id == GROUP_ID)
channel_rt.channel_post.filter(F.chat.id == CHANNEL_ID)

private_rt.chat_member.filter(F.chat.type == ChatType.PRIVATE)
group_rt.chat_member.filter(F.chat.id == GROUP_ID)
channel_rt.chat_member.filter(F.chat.id == CHANNEL_ID)

dp.include_routers(group_rt, private_rt, channel_rt)


group_rt.chat_member.register(welcome, ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
