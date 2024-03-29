import asyncio
import subprocess
import os
from pythonping import ping

from aiogram import Bot, Dispatcher, executor
from config import BOT_TOKEN, IP, URL

loop = asyncio.get_event_loop()
bot: Bot = Bot(BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, loop=loop)


async def main(dp: Dispatcher):
    await bot.set_webhook(URL)
    old_response = ""

    while True:
        # response = subprocess.getstatusoutput("ping -c 1 " + IP)
        response = ping(IP, verbose=True)
        print(response)
        if old_response != response:
            if response == "Request timed out":
                await lights_off(dp)
                old_response = response
            else:
                await lights_on(dp)
                old_response = response


async def on_shutdown(dp):
    await bot.delete_webhook()


if __name__ == "__main__":
    from handlers import lights_off, lights_on

    executor.start_webhook(
        dispatcher=dp,
        webhook_path="",
        on_startup=main,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
    )
    # executor.start_polling(dp, on_startup=main)
