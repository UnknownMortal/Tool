from pyrogram.types import Message
import asyncio
import asyncio
from pyrogram import filters, Client
from tool.sos.help import *

@Client.on_message(filters.me & filters.command(["dspam", "deletespam"], [".", "!", "/"]))
async def statspam(client: Client, message: Message):
    tool = await message.reply_text("Usage : /dspam 10 Hello 👋")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    await message.delete()
    for i in range(quantity):
        await tool.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.1)
        await msg.delete()
        await asyncio.sleep(0.1)


@Client.on_message(filters.me & filters.command(["spam", "spamming"], [".", "!", "/"]))
async def sspam(client: Client, message: Message):
    tool = await message.reply_text("usage : /spam 10 Hello 👋")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.15)
        return

    for _ in range(quantity):
        await tool.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.15)


@Client.on_message(filters.me & filters.command(["fastspam"], [".", "!", "/"]))
async def fastspam(client: Client, message: Message):
    tool = await message.reply_text("Usage : /fastspam 10 hello 👋")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)
    
    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(0.002)
        return
    
    for _ in range(quantity):
        await tool.delete()
        await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(0.002)



@Client.on_message(filters.me & filters.command(["slowspam", "delayspam"], [".", "!", "/"]))
async def slowspam(client: Client, message: Message):
    tool = await message.reply_text("Usage : .slowspam 10 Hello 👋")
    quantity = message.command[1]
    spam_text = ' '.join(message.command[2:])
    quantity = int(quantity)

    if message.reply_to_message:
        reply_to_id = message.reply_to_message.message_id
        for _ in range(quantity):
            await client.send_message(message.chat.id, spam_text,
                                      reply_to_message_id=reply_to_id)
            await asyncio.sleep(1.5)
        return

    for _ in range(quantity):
        await tool.delete()
        msg = await client.send_message(message.chat.id, spam_text)
        await asyncio.sleep(1.5)


@Client.on_message(filters.me & filters.command(["sspam", "stkspam", "spamstk", "stickerspam"], [".", "!", "/"]))
async def spam_stick(client: Client, message: Message):
    if not message.reply_to_message:
        await message.edit_text("**reply to a sticker with amount you want to spam**")
        return
    if not message.reply_to_message.sticker:
        await message.edit_text(text="**reply to a sticker with amount you want to spam**")
        return
    else:
        i=0
        times = message.command[1]
        if message.chat.type in ["supergroup", "group"]:
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id,
                    sticker,
                )
                await asyncio.sleep(0.10)

        if umm.chat.type == "private":
            for i in range(int(times)):
                sticker=message.reply_to_message.sticker.file_id
                await client.send_sticker(
                    message.chat.id, sticker
                )
                await asyncio.sleep(0.10)


add_command_help(
    "Spam",
    [
        [".dspam", "It will Spam then delete it's spam automatically."],
        [".spam", "Spam Your Custom Message  (Sudo User also)."],
        [".sspam", "Sticker Spam  (Sudo Users also)."],
        [".delayspam", "Spam Slowly (Sudo User also)."],
        [".fastspam", "Spam Your message fastly  (Sudo User also)."],
    ],
)
