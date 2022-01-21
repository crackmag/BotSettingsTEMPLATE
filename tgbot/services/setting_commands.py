from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeChat, BotCommandScopeDefault, BotCommandScopeAllGroupChats, \
    BotCommandScopeAllPrivateChats, BotCommandScopeAllChatAdministrators, BotCommandScopeChatAdministrators, \
    BotCommandScopeChatMember

# lang_code можно взять тут (ISO 639-1):
# https://www.loc.gov/standards/iso639-2/php/code_list.php
STARTING_COMMANDS = {
    'ru': [
        BotCommand('start', 'Начать заново'),
        BotCommand('get_commands', 'Получить список команд'),
        BotCommand('reset_commands', 'Сбросить команды'),
    ],
    'en': [
        BotCommand('start', 'Restart bot'),
        BotCommand('get_commands', 'Retrieve command list'),
        BotCommand('reset_commands', 'Reset Commands'),
    ]
}


async def set_starting_commands(bot: Bot, chat_id: int):
    """
    Назначает команды бота только для определенного чата.

    :param bot: экземпляр бота, которым будет выполняться команда.
    :param chat_id: Идентификатор чата, где будут назначены команды.
    """
    for language_code, commands in STARTING_COMMANDS.items():
        await bot.set_my_commands(
            commands=commands,
            scope=BotCommandScopeChat(chat_id),
            language_code=language_code
        )


async def reset_commands(bot: Bot, chat_id: int):
    await bot.delete_my_commands(scope=BotCommandScopeChat(chat_id))


async def force_reset_all_commands(bot: Bot):
    for language_code in ('ru', 'en', 'uk', 'uz'):
        for scope in (
                BotCommandScopeAllGroupChats(),
                BotCommandScopeAllPrivateChats(),
                BotCommandScopeAllChatAdministrators(),
                BotCommandScopeDefault(),
        ):
            await bot.delete_my_commands(scope, language_code)


async def set_default_commands(bot: Bot):
    """
    Назначает стандартные команды бота во всех чатах.

    :param bot: экземпляр бота, которым будет выполняться команда.
    :return: Возвращает True в случае успешного выполнения.
    """
    return await bot.set_my_commands(
        commands=[
            BotCommand('change_commands', 'Изменить команды в личных чатах'),
            BotCommand('command_default_1', 'Стандартная команда 1'),
            BotCommand('command_default_2', 'Стандартная команда 2'),
            BotCommand('command_default_3', 'Стандартная команда 3'),
            BotCommand('command_default_4', 'Стандартная команда 4'),
        ],
        scope=BotCommandScopeDefault()
    )


async def set_all_private_commands(bot: Bot):
    """
    Назначает команды бота для участников всех личных чатов с ботом.

    :param bot: экземпляр бота, которым будет выполняться команда.
    :return: Возвращает True в случае успешного выполнения.
    """
    await bot.delete_my_commands(scope=BotCommandScopeAllPrivateChats())
    return await bot.set_my_commands(
        commands=[
            BotCommand('account', 'Настройки аккаунта'),
            BotCommand('wallet', 'Кошелек'),
            BotCommand('reset_commands', 'Сбросить команды'),
        ],
        scope=BotCommandScopeAllPrivateChats()
    )


async def set_all_group_commands(bot: Bot):
    """
    Назначает команды бота для участников всех групповых чатов.

    :param bot: экземпляр бота, которым будет выполняться команда.
    :return: Возвращает True в случае успешного выполнения.
    """
    return await bot.set_my_commands(
        commands=[
            BotCommand('start', 'Информация о боте'),
            BotCommand('report', 'Пожаловаться на пользователя'),
        ],
        scope=BotCommandScopeAllGroupChats()
    )


async def set_all_chat_admins_commands(bot: Bot):
    """
    Назначает команды бота для Администраторов всех групповых чатов.

    :param bot: экземпляр бота, которым будет выполняться команда.
    :return: Возвращает True в случае успешного выполнения.
    """
    return await bot.set_my_commands(
        commands=[
            BotCommand('ro', 'Мут пользователя'),
            BotCommand('ban', 'Забанить пользователя'),
            BotCommand('change_commands', 'Изменить команды в этом чате'),
        ],
        scope=BotCommandScopeAllChatAdministrators()
    )


async def set_chat_admins_commands(bot: Bot, chat_id: int):
    """
    Назначает команды бота только для Администраторов определенного группового чата.

    :param bot: экземпляр бота, которым будет выполняться команда.
    :param chat_id: Идентификатор чата, где будут назначены команды.
    :return: Возвращает True в случае успешного выполнения.
    """
    return await bot.set_my_commands(
        commands=[
            BotCommand('ro', 'Мут пользователя'),
            BotCommand('ban', 'Забанить пользователя'),
            BotCommand('reset_commands', 'Сбросить команды'),
        ],
        scope=BotCommandScopeChatAdministrators(chat_id)
    )


async def set_chat_member_commands(bot: Bot, chat_id: int, user_id: int):
    """
    Назначает команды бота только для Администраторов определенного группового чата.

    :param bot: экземпляр бота, которым будет выполняться команда.
    :param chat_id: Идентификатор чата, где будут назначены команды.
    :param user_id: Идентификатор пользователя, которому будут назначены команды.
    :return: Возвращает True в случае успешного выполнения.
    """
    return await bot.set_my_commands(
        commands=[
            BotCommand('kick_me', 'Выйти из чата'),
        ],
        scope=BotCommandScopeChatMember(chat_id, user_id)
    )
