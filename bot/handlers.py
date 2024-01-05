from aiogram import types
from config import bot, WELCOME_IMAGE_LINK, OWNER_ID

import logging
import sys


logging.basicConfig(
    level=logging.DEBUG,
    format='''[%(asctime)s] #%(levelname)-8s %(filename)s:
%(lineno)d - %(name)s - %(message)s''',
    filename='logs/handlers.log',
    filemode='a'
)
logger = logging.getLogger(__name__)

stdout_handler = logging.StreamHandler(sys.stdout)
logger.addHandler(stdout_handler)


async def welcome(event: types.ChatMemberUpdated):

    logger.info(f'handler works - welcome function started. User id={event.new_chat_member.user.id} joined group chat')

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

    logger.info('welcome function finished')


async def start_private(message: types.Message):

    logger.info(f'handler works - start_private function started by user id={message.from_user.id}')

    await message.reply('''Приветик👋👋
здесь ты можешь связаться с админами канала. Просто отправляй сообщения, мы постараемся ответить''')

    logger.info('start_private function finished')


async def copy(message: types.Message):

    await message.copy_to(chat_id=OWNER_ID)
