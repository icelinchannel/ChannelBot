from aiogram import Bot, Dispatcher, F, Router, types

from aiogram.enums.chat_type import ChatType

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

import asyncio

from config import API_TOKEN, WELCOME_IMAGE_LINK, CHAT_ID, CHANNEL_ID


bot = Bot(API_TOKEN)
dp = Dispatcher()

private_rt = Router()
group_rt = Router()
channel_rt = Router()


private_rt.message.filter(F.chat.type == ChatType.PRIVATE)
group_rt.message.filter(F.chat.id == CHAT_ID)
channel_rt.message.filter(F.chat.id == CHANNEL_ID)

private_rt.channel_post.filter(False)
group_rt.channel_post.filter(False)
channel_rt.channel_post.filter(True)

private_rt.chat_member.filter(F.chat.type == ChatType.PRIVATE)
group_rt.chat_member.filter(F.chat.id == CHAT_ID)
channel_rt.chat_member.filter(F.chat.type == ChatType.CHANNEL)

dp.include_routers(group_rt, private_rt, channel_rt)


@group_rt.chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def welcome(event: types.ChatMemberUpdated):

    if event.from_user.username[-3:] != 'bot':
        await event.answer_photo(
            photo=WELCOME_IMAGE_LINK,
            caption=f'''🔴Привет, [{event.from_user.full_name}](https://t.me/{event.from_user.username})👋👋👋

Добро пожаловать в чат\. У нас тут правила, всё как везде:

👉 Уважайте других, относитесь к ним так, как хотите, чтобы относились к вам

👉 Никого не оскорбляйте, не нужно плодить агрессию\. Давайте лучше распространять доброе общение\)

👉 Никакой рекламы в чате, понятно?😉

👉 Не присылайте сюда шокирующий контент и порнографию

👉 Мы оставляем за собой право удалять любые сообщения и пользователей из группы

❗️ Занудство закончилось, можно писать\)''',
        parse_mode='MarkdownV2'
    )

    else:
        bot.ban_chat_member(chat_id=CHAT_ID, revoke_messages=True, user_id=event.from_user.id)


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
