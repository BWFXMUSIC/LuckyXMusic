from AarohiX import app
import asyncio
from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from AarohiX.misc import SUDOERS
from pyrogram import Client, filters, enums
from pyrogram.errors import UserAlreadyParticipant
import random
from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from pyrogram.errors import (
    ChatAdminRequired,
    InviteRequestSent,
    UserAlreadyParticipant,
    UserNotParticipant,
)

async def get_dialog_count(dialog_type, userbot):
    count = 0
    async for dialog in userbot.get_dialogs():
        if dialog_type == "GROUP" and dialog.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
            count += 1
        elif dialog_type == "USERS" and dialog.chat.type == enums.ChatType.PRIVATE:
            count += 1
        elif dialog_type == "CHANNELS" and dialog.chat.type == enums.ChatType.CHANNEL:
            count += 1
    return count


async def get_bot_statss(userbot):
    group_count = await get_dialog_count("GROUP", userbot)
    user_count = await get_dialog_count("USERS", userbot)
    channel_count = await get_dialog_count("CHANNELS", userbot)
    return {"Groups": group_count, "Users": user_count, "Channels": channel_count}

@app.on_message(filters.command("botstats"))
async def bot_statss(client, message):   
  chat_id = message.chat.id
  userbot = await get_assistant(message.chat.id)
  userbot_id = userbot.id
  stats = await get_bot_statss(userbot)        
  stats_text = "\n".join([f"{key}: {value}" for key, value in stats.items()])   
  await message.reply(f"Bot Stats:\n{stats_text}")