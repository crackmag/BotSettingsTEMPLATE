from aiogram import Dispatcher
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, ChatType, BotCommandScopeChat
from aiogram.utils.markdown import quote_html

from tgbot.services.setting_commands import set_all_private_commands, set_chat_admins_commands, reset_commands


async def get_bot_commands(message: Message):
    commands = await message.bot.get_my_commands(BotCommandScopeChat(message.from_user.id))
    await message.answer(quote_html(str(commands)))


async def change_private_commands(message: Message):
    if await set_all_private_commands(message.bot):
        await message.answer('Все Приватные команды были изменены.')
    else:
        await message.answer('Что-то пошло не так.')


async def reset_all_commands(message: Message):
    await reset_commands(message.bot, message.chat.id)
    await message.answer('Все Команды были сброшены.')


async def change_admin_commands(message: Message):
    if await set_chat_admins_commands(message.bot, message.chat.id):
        await message.answer('Команды администраторов для этого чата были изменены.')
    else:
        await message.answer('Что-то пошло не так.')


def register_setting_commands(dp: Dispatcher):
    dp.register_message_handler(get_bot_commands, Command('get_commands'), chat_type=ChatType.PRIVATE)
    dp.register_message_handler(reset_all_commands, Command('reset_commands'))
    dp.register_message_handler(change_private_commands, Command('change_private_commands'), chat_type=ChatType.PRIVATE)
    dp.register_message_handler(change_admin_commands, Command('change_commands'), chat_type=ChatType.SUPERGROUP)
