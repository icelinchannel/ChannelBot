from aiogram import types, F

from aiogram.enums.chat_type import ChatType

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

from config import bot, WELCOME_IMAGE_LINK, GROUP_ID, CHANNEL_ID, private_rt, group_rt, channel_rt, dp
import filters


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
        await bot.ban_chat_member(chat_id=GROUP_ID, revoke_messages=True, user_id=event.from_user.id)
