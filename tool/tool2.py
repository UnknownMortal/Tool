from pyrogram import filters, Client
from pyrogram.types import *
from main import *
from tool.sos.help import *


@Client.on_message(filters.me & filters.command(["directmessage", "dm", "msg"], [".", "!", "/"]))
async def dm(client: Client, message: Message):
    tool = await message.reply_text("/dm or /msg @username Hello 👋")
    quantity = 1
    inp = message.text.split(None, 2)[1]
    user = await client.get_chat(inp)
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await tool.edit("Message Sended Successfully ✅")
            await client.send_message(user.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(user.id, spam_text)
        await tool.edit("Message Sended Successfully ✅")
        await asyncio.sleep(0.15)

@Client.on_message(filters.user(SUDO_USERS) & filters.command(["directmessage", "dm", "msg"], [".", "!", "/"]))
async def dmm(client: Client, message: Message):
    tool = await message.reply_text("/dm or /msg @username Hello 👋")
    quantity = 1
    inp = message.text.split(None, 2)[1]
    user = await client.get_chat(inp)
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await tool.edit("Message Sended Successfully ✅")
            await client.send_message(user.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await client.send_message(user.id, spam_text)
        await tool.edit("Message Sended Successfully ✅")
        await asyncio.sleep(0.15)
