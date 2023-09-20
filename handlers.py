from main import bot
from config import GROUP_ID, LIGHTS_ON_TEXT, LIGHTS_OFF_TEXT


async def lights_on(dp):
    await bot.send_message(chat_id=GROUP_ID, text=LIGHTS_ON_TEXT)


async def lights_off(dp):
    await bot.send_message(chat_id=GROUP_ID, text=LIGHTS_OFF_TEXT)