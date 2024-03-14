
import math
from config import SUPPORT_CHANNEL, OWNER_ID
from pyrogram.types import InlineKeyboardButton

from AarohiX.utils.formatters import time_to_seconds


def track_markup(_, videoid, user_id, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            )
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥𝐎𝚆𝙽𝙴𝚁❤️‍🔥", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="💝𝐉𝙰𝙰𝙽💝", url=SUPPORT_CHANNEL,
            )
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def stream_markup_timer(_, chat_id, played, dur):
    played_sec = time_to_seconds(played)
    duration_sec = time_to_seconds(dur)
    percentage = (played_sec / duration_sec) * 100
    top = math.floor(percentage)
    if 0 < top <= 10:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ❤️"
    elif 10 < top < 20:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ❤️٨ـ"
    elif 20 <= top < 30:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨ـ❤️ﮩﮩ٨ـ"
    elif 30 <= top < 40:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ٨❤️ـﮩﮩ٨ـ"
    elif 40 <= top < 50:
        bar = "ﮩ٨ـﮩﮩ٨ـﮩ❤️٨ـﮩﮩ٨ـ"
    elif 50 <= top < 60:
        bar = "ﮩ٨ـﮩﮩ٨❤️ـﮩ٨ـﮩﮩ٨ـ"
    elif 60 <= top < 70:
        bar = "ﮩ٨ـﮩ❤️ﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 70 <= top < 80:
        bar = "ﮩ٨❤️ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    elif 80 <= top < 95:
        bar = "ﮩ❤️٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    else:
        bar = "❤️ﮩ٨ـﮩﮩ٨ـﮩ٨ـﮩﮩ٨ـ"
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{played} {bar} {dur}",
                callback_data="GetTimer",
            )
        ],
        [
            InlineKeyboardButton(text="❣️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="❤️", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="💞", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="💔", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="❤️‍🩹", callback_data=f"ADMIN Stop|{chat_id}")
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥𝐎𝚆𝙽𝙴𝚁❤️‍🔥", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="💝𝐉𝙰𝙰𝙽💝", url=SUPPORT_CHANNEL,
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def stream_markup(_, chat_id):
    buttons = [
        [
            InlineKeyboardButton(text="❣️", callback_data=f"ADMIN Resume|{chat_id}"),
            InlineKeyboardButton(text="❤️", callback_data=f"ADMIN Pause|{chat_id}"),
            InlineKeyboardButton(text="💞", callback_data=f"ADMIN Replay|{chat_id}"),
            InlineKeyboardButton(text="💔", callback_data=f"ADMIN Skip|{chat_id}"),
            InlineKeyboardButton(text="❤️‍🩹", callback_data=f"ADMIN Stop|{chat_id}")
        ],
        [
            InlineKeyboardButton(
                text="❤️‍🔥𝐎𝚆𝙽𝙴𝚁❤️‍🔥", url=f"tg://openmessage?user_id={OWNER_ID}",
            ),
            InlineKeyboardButton(
                text="💝𝐉𝙰𝙰𝙽💝", url=SUPPORT_CHANNEL,
            )
        ],
        [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data="close")],
    ]
    return buttons


def playlist_markup(_, videoid, user_id, ptype, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"DilPlaylists {videoid}|{user_id}|{ptype}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"DilPlaylists {videoid}|{user_id}|{ptype}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def livestream_markup(_, videoid, user_id, mode, channel, fplay):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_3"],
                callback_data=f"LiveStream {videoid}|{user_id}|{mode}|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def slider_markup(_, videoid, user_id, query, query_type, channel, fplay):
    query = f"{query[:20]}"
    buttons = [
        [
            InlineKeyboardButton(
                text=_["P_B_1"],
                callback_data=f"MusicStream {videoid}|{user_id}|a|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["P_B_2"],
                callback_data=f"MusicStream {videoid}|{user_id}|v|{channel}|{fplay}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="◁",
                callback_data=f"slider B|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"],
                callback_data=f"forceclose {query}|{user_id}",
            ),
            InlineKeyboardButton(
                text="▷",
                callback_data=f"slider F|{query_type}|{query}|{user_id}|{channel}|{fplay}",
            ),
        ],
    ]
    return buttons
