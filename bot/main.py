from aiogram import Bot, Dispatcher, F, Router, types

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION
from aiogram.types import ChatMemberUpdated

import asyncio

from config import API_TOKEN


bot = Bot(API_TOKEN)
dp = Dispatcher()

privat_rt = Router()
community_rt = Router()

privat_rt.message.filter(F.chat.type == 'privat')
community_rt.message.filter(F.chat.type == 'group')
