import asyncio
import os

from aiogram import Bot, Dispatcher, executor

from config import BOT_TOKEN, IP

loop = asyncio.get_event_loop()
bot = Bot(BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher(bot, loop=loop)


async def main(dp):
    old_response = ''
    response = os.system('ping -c 1 ' + IP)
    if old_response != response:
        if response == 0:
            await lights_on(dp)
            old_response = response
        else:
            await lights_off(dp)
            old_response = response


if __name__ == '__main__':
    from handlers import lights_off, lights_on
    executor.start_polling(dp, on_startup=main)

