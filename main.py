import os
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from handlers.user_private import user_private_router
from handlers.user_group import user_group_router
from common.bot_commands_list import private


ALLOWED_UPDATES = ['message, edited_message']

bot = Bot(token=os.getenv('TOKEN'), parse_mode=ParseMode.HTML)
dp = Dispatcher()

dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
  logging.basicConfig(level=logging.INFO, stream=sys.stdout)
  # чтобы бот не аккумулировал запросы, когда он не запущен. 
  # А отвечал только, когда он запущен (онлайн)
  await bot.delete_webhook(drop_pending_updates=True) 
  await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
  await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)

asyncio.run(main())