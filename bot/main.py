from aiogram import Bot, Dispatcher, F

from aiogram.enums.chat_type import ChatType

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

import asyncio

from config import bot, dp, private_rt, group_rt, channel_rt, CHANNEL_ID, GROUP_ID
from handlers import welcome


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
