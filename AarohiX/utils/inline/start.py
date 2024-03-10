from pyrogram.types import InlineKeyboardButton

import config
from AarohiX import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_1"], url=f"https://t.me/{app.username}?startgroup=true"
            ),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐇𝙴𝙻𝙿 ۞", callback_data="settings_back_helper"),
            InlineKeyboardButton(
                text="☢ 𝐒𝙴𝚃 ☢", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="✡ 𝐆𝚁𝙾𝚄𝙿 ✡", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_3"],
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(text="𝐆𝚁𝙾𝚄𝙿✨", url=config.SUPPORT_CHAT),
            InlineKeyboardButton(text="𝚂𝙷𝙰𝚈𝚁𝙸🥀", url=config.SUPPORT_CHANNEL),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐅𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ۞", callback_data="settings_back_helper")
        ],
        [
InlineKeyboardButton(text="𝐒𝚃𝚄𝙳𝚈", url=f"https://t.me/+UQUsfzMdlIJjNjll"),
            InlineKeyboardButton(text="𝟹ᴅ ᴀɪ ᴅᴘ", url=f"https://t.me/DP_AI_DP"),
        ],
    ]

    return buttons
