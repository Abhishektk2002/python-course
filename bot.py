import asyncio
from config import *
from telethon import TelegramClient, events

async def main():
    bot = await TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    print("signed in")
    @bot.on(events.NewMessage())
    async def handle_message(message):
       await message.reply("Hello")
    await bot.run_until_disconnect()
asyncio.run(main())