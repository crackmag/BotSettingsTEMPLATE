import asyncio
import logging

from aiogram import Bot

from tgbot.config import Config


async def send_messages(bot: Bot, config: Config):
    for user_id in config.tg_bot.admin_ids:
        try:
            await bot.send_message(user_id, 'Бот был запущен')
        except Exception as er:
            logging.exception(er)
        finally:
            await asyncio.sleep(0.05)
