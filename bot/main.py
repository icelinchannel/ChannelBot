from aiogram import Bot, Dispatcher, F, Router, types

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

import asyncio

from config import API_TOKEN


bot = Bot(API_TOKEN)
dp = Dispatcher()

private_rt = Router()
community_rt = Router()

private_rt.message.filter(F.chat.type == 'privat')
community_rt.message.filter(F.chat.type == 'group')
community_rt.chat_member.filter(F.chat.type == 'group')

dp.include_routers(community_rt, private_rt)


@community_rt.chat_member(ChatMemberUpdatedFilter(JOIN_TRANSITION))
async def welcome(event: types.ChatMemberUpdated):
    return event.reply_photo(photo='images/hello.jpg', caption='''Добро пожаловать в чат👋👋👋
🔴 У нас тут правила чата, всё как везде:

👉 Уважайте других, относитесь к ним так, как хотите, чтобы относились к вам

👉 Никого не оскорбляйте, не нужно плодить агрессию. Давайте лучше распространять доброе общение)

👉 Никакой рекламы в чате, понятно?😉

👉 Не присылайте сюда шокирующий контент и порнографию

👉 Мы оставляем за собой право удалять любые сообщения и пользователей из группы

❗️ Занудство закончилось, можно писать)''')


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
