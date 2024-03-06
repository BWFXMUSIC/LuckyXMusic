import asyncio
import datetime
from AarohiX import app
from pyrogram import Client
from AarohiX.utils.database import get_served_chats
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


START_IMG_URL = "https://te.legra.ph/file/d03391a86b480004e86e2.jpg"


MESSAGE = f"""🎉 ᴀ ʙɪɢ sʜᴏᴜᴛᴏᴜᴛ ᴛᴏ ᴏᴜʀ ɴᴇᴡᴇsᴛ ᴍᴇᴍʙᴇʀ! 🙏 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ɢʀᴏᴜᴘ ᴡʜᴇʀᴇ ᴄᴏɴᴠᴇʀsᴀᴛɪᴏɴs ᴄᴏᴍᴇ ᴛᴏ ʟɪғᴇ. 🗣️ ᴅɪᴠᴇ ɪɴ, ɪɴᴛʀᴏᴅᴜᴄᴇ ʏᴏᴜʀsᴇʟғ, ᴀɴᴅ ʟᴇᴛ's ᴋɪᴄᴋ ᴏғғ sᴏᴍᴇ ᴀᴍᴀᴢɪɴɢ ᴄʜᴀᴛs. ᴄʟɪᴄᴋ ᴛʜᴇ ʟɪɴᴋ ᴛᴏ ᴊᴏɪɴ ᴛʜᴇ ғᴜɴ – ᴡᴇ'ᴠᴇ ʙᴇᴇɴ ᴡᴀɪᴛɪɴɢ ғᴏʀ ʏᴏᴜ! 🌟 #ʜᴇʀᴏᴄᴏᴍᴍᴜɴɪᴛʏ"

💞ᴊᴏɪɴ » [✘ ᴄʟɪᴄᴋ ᴍᴇ ✘](https://t.me/rajabhaiya2u) <√ᴊᴏɪɴ ᴏᴜʀ ғᴀᴍɪʟʏ ɢʀᴏᴜᴘ.^>

🚩 ʙᴏᴛ »|| @{app.username}||"""

BUTTON = InlineKeyboardMarkup(
 [
        [
InlineKeyboardButton("ʜᴇʟᴘ", url="https://t.me/https://t.me/+g0YcEKl54yU0ZTU9"),
          InlineKeyboardButton("ᴏᴡɴᴇʀ", url="https://t.me/LuckyRaja0"),
        ],
        [
          InlineKeyboardButton("𝙶𝙸𝚃𝙷𝚄𝙱 𝙸𝙳", url=f"https://github.com/THE-TOP-BOY"),
          InlineKeyboardButton("︎𝚃𝙾𝙿 𝙼𝚄𝚂𝙸𝙲", url=f"https://github.com/THE-TOP-BOY/TOP-MUSIC"),
        ],
        [
          InlineKeyboardButton("𝙸𝙽𝚂𝚃𝙰 𝙸𝙳", url=f"https://www.instagram.com/itz_lucky.raja?igsh=ajFtZDRmbTZoaHY5"),
          InlineKeyboardButton("𝟹𝙳 𝙰𝙸 𝙳𝙿", url=f"https://t.me/DP_AI_DP"),
        ],
        [
          InlineKeyboardButton("𝚀𝚄𝙸𝚉 𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/+wsMlyxTvQtYwN2Y1"),
          InlineKeyboardButton("𝚃𝙾𝚃𝙰𝙻 𝚀𝚄𝙸𝚉", url=f"https://t.me/T_Quiz"),
        ],
        [
          InlineKeyboardButton("𝙼𝙰𝚂𝚃𝙸 𝙶𝚁𝙾𝚄𝙿 ", url="https://t.me/+YFFVeXdYxkQ1ODhl"),
          InlineKeyboardButton("बदनाम मोहब्बत", url=f"https://t.me/Badnam_Mohabbat"),
        ],
        [
          InlineKeyboardButton("TOP TG BOTS", url=f"https://t.me/TOP_TG_BOTS"),
          InlineKeyboardButton("TOP TG FRIENDS", url=f"TOP_TG_FRIENDS"),
        ],
        [
          InlineKeyboardButton("𝙵𝙸𝚁𝚂𝚃 𝙸𝙳", url=f"https://t.me/THE_OP_BOY"),
          InlineKeyboardButton("𝚂𝙴𝙲𝙾𝙽𝙳 𝙸𝙳", url=f"https://t.me/THE_TOP_BOY_OP"),
        ],
        [
          InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/ZiddiXBot"),
    [
        [
            InlineKeyboardButton("» ᴀᴅᴅ ᴍᴇ «", url=f"https://t.me/{app.username}?startgroup=s&admin=delete_messages+manage_video_chats+pin_messages+invite_users")
        ]
    ]
)

async def send_message_to_chats():
    try:
        chats = await get_served_chats()

        for chat_info in chats:
            chat_id = chat_info.get('chat_id')
            if isinstance(chat_id, int):  
                try:
                    await app.send_photo(chat_id, photo=START_IMG_URL, caption=MESSAGE, reply_markup=BUTTON)
                    await asyncio.sleep(3)
                except Exception as e:
                    pass  
    except Exception as e:
        pass  

async def continuous_broadcast():
    while True:
        await send_message_to_chats()
        await asyncio.sleep(50000)  
        
asyncio.create_task(continuous_broadcast())
