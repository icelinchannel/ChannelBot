from aiogram import types
from config import bot, WELCOME_IMAGE_LINK

import logging
import sys


logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
       '%(lineno)d - %(name)s - %(message)s',
    style='{',
    filename='logs/main.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

stderr_handler = logging.StreamHandler()
stdout_handler = logging.StreamHandler(sys.stdout)

logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)


async def welcome(event: types.ChatMemberUpdated):

    logger.info('Handler works - function started')

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


async def start_private(message: types.Message):

    logger.info('Handler works - function started')

    await message.reply('''Приветик👋👋
здесь ты можешь связаться с админами канала. Просто отправляй сообщения, мы постараемся ответить''')
