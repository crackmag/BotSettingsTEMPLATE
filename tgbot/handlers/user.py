from aiogram import Dispatcher
from aiogram.types import Message, BotCommandScopeChat, ChatType
from aiogram.utils.markdown import quote_html

from tgbot.services.setting_commands import set_starting_commands, set_chat_admins_commands


async def user_start(message: Message):
    await message.reply("Hello, user!")
    await set_starting_commands(message.bot, message.from_user.id)


async def message_get_commands(message: Message):

    no_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id))
    no_args = await message.bot.get_my_commands()
    en_lang = await message.bot.get_my_commands(scope=BotCommandScopeChat(message.from_user.id),
                                                language_code='en')
    await message.reply("\n\n".join(
        f'<pre>{quote_html(arg)}</>' for arg in (no_args, no_lang, en_lang)
    ))


async def message_reset_commands(message: Message):
    await message.bot.delete_my_commands(BotCommandScopeChat(message.from_user.id),
                                         language_code='en')
    await message.reply('Команды были удалены')


async def change_admin_commands(message: Message):
    await set_chat_admins_commands(message.bot, message.chat.id)
    await message.answer('Команды администраторов для этого чата были изменены.')


def register_user(dp: Dispatcher):
    dp.register_message_handler(user_start, commands=["start"], state="*")
    dp.register_message_handler(message_get_commands, commands=["get_commands"])
    dp.register_message_handler(message_get_commands, commands=["get_commands_chat"])
    dp.register_message_handler(message_reset_commands, commands=["reset_commands"])
    dp.register_message_handler(change_admin_commands, commands=["change_commands"],
                                chat_type=ChatType.SUPERGROUP)
