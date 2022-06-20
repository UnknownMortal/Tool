from pyrogram import Client , filters
import asyncio
from pyrogram.types import Message

from tool.sos.help import *

@Client.on_message(filters.command(["inviteall", "kidnapall", "scrap"], [".", "!", "#", "/"]) & filters.me)
async def inv(client: Client, message: Message):
    tool = await message.reply_text("Also give the Target group's username or link to invite members in your Group !!")
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await tool.edit_text(f"Inviting users from : {chat.username}")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online", "offline" , "recently", "within_week"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg = await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            await mg.delete()
