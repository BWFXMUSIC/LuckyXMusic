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
            InlineKeyboardButton(text="❤️‍🔥𝐎𝚆𝙽𝙴𝚁❤️‍🔥", user_id=config.OWNER_ID),
            InlineKeyboardButton(text="💝𝐉𝙰𝙰𝙽💝", user_id=5493923823),
        ],
        [
            InlineKeyboardButton(text="۞ 𝐅𝙴𝙰𝚃𝚄𝚁𝙴𝚂 ۞", callback_data="settings_back_helper")
        ],
        [
InlineKeyboardButton(text="𝐒𝚃𝚄𝙳𝚈", url=f"https://t.me/+UQUsfzMdlIJjNjll"),
            InlineKeyboardButton(text="𝚃 𝚀𝚄𝙸𝚉", url=f"https://t.me/T_QUIZ"),
        ],
        [
InlineKeyboardButton(text=_["S_B_5"], user_id=config.OWNER_ID),
            InlineKeyboardButton(text=_["S_B_6"], url=config.SUPPORT_CHANNEL),
            InlineKeyboardButton(text=_["S_B_2"], url=config.SUPPORT_CHAT),
        ],
        [
InlineKeyboardButton(text=_["S_B_7"], url=f"https://github.com/Lippsxd/LippsMusicBot")
        ],
    ]

    return buttons
