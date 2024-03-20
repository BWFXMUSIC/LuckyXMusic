import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()


API_ID = int(getenv("API_ID", "28178139"))

API_HASH = getenv("API_HASH", "85172511f45230b7f8bb304f5ed8e6d8")

BOT_TOKEN = getenv("BOT_TOKEN", "")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://Lucky:RajaOp@atlascluster.f7lck9c.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1001764180763"))

OWNER_ID = int(getenv("OWNER_ID", "5247304559"))

BOT_USERNAME = getenv("BOT_USERNAME" , "RuhiMusicBot")

COMMAND_HANDLER = getenv("COMMAND_HANDLER", "! / .").split()

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/THE-TOP-BOY/LuckyXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/Badnam_Mohabbat")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/+WDNH4yTCWe5jOTI1")

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/b6edf7d9c8905fc62657c.png"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/5899524dee3c817fa07bd.png"
)
PLAYLIST_IMG_URL = "https://graph.org/file/faf885e67926960b853a3.jpg"
STATS_IMG_URL = "https://telegra.ph/file/1d246bd7d1a05d9324a1b.png"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/77589cbc8d160feca84f8.png"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/c60fb43eff43af783457f.png"
STREAM_IMG_URL = "https://telegra.ph/file/fe3a4103dd7c2f5933b5e.png"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/c90660ae43617d281ced5.png"
YOUTUBE_IMG_URL = "https://graph.org/file/e9eb24350ac3fa98bc49d.mp4"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/3c69795ea004b98f6e23c.png"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/088dbf9470835d529dce3.png"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/08cc4e128139348db1878.png"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
