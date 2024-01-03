from aiogram import types

from config import bot, WELCOME_IMAGE_LINK, GROUP_ID


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


async def start_private(command: types.Message):
    await command.reply('''Приветик👋👋
здесь ты можешь связаться с админами канала. Просто отправляй сообщения, мы постараемся ответить''')
