from aiogram import F, types

from aiogram.filters.command import Command
from aiogram.enums.chat_type import ChatType

from aiogram.filters import ChatMemberUpdatedFilter
from aiogram.filters.chat_member_updated import JOIN_TRANSITION

import asyncio

from config import bot, dp, private_rt, group_rt, channel_rt, CHANNEL_ID, GROUP_ID, WELCOME_IMAGE_LINK
from handlers import welcome, start_private
from filters import PrivateRouterFilter, GroupRouterFilter, ChannelRouterFilter


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


@group_rt.chat_member(ChatMemberUpdatedFilter(member_status_changed=JOIN_TRANSITION))
async def welcome(event: types.ChatMemberUpdated):

    if event.new_chat_member.user.is_bot is False:

        name_with_link = f'[{event.new_chat_member.user.full_name}]({event.new_chat_member.user.username})'
        name_without_link = event.new_chat_member.user.full_name

        await event.answer_photo(
            photo=WELCOME_IMAGE_LINK,
            caption=f'''🔴Привет, {name_without_link if type(event.new_chat_member.user.username) is None else name_with_link}👋👋👋

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
        await event.answer('Ботам не место в чате!')
        await bot.ban_chat_member(revoke_messages=True, chat_id=event.chat.id, user_id=event.new_chat_member.user.id)

@private_rt.message(Command('start'))
async def start_private(command: types.Message):
    await command.reply('''Приветик👋👋
здесь ты можешь связаться с админами канала. Просто отправляй сообщения, мы постараемся ответить''')


async def start():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(start())
