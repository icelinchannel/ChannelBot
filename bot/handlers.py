from aiogram import types

from config import bot, WELCOME_IMAGE_LINK, GROUP_ID


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


async def bot_added_to_another_group(event: types.ChatMemberUpdated):
    await event.answer('Стоооп... Я создан не для этого чата, до свидания')
    await bot.leave_chat(chat_id=event.chat.id)
