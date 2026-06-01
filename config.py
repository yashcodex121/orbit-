import os
import shutil

class Config:
    API_ID = int(os.getenv("API_ID"))
    API_HASH = os.getenv("API_HASH")
    BOT_TOKEN = os.getenv("BOT_TOKEN")

    MONGO_URI = os.getenv("MONGO_URI")
    DB_NAME = os.getenv("DB_NAME", "music_bot")

    DOWNLOAD_DIR = "downloads"

    MAX_FILE_SIZE = 50 * 1024 * 1024

    FFMPEG_PATH = shutil.which("ffmpeg") or "ffmpeg"

    OWNER_IDS = [
        int(x)
        for x in os.getenv("OWNER_IDS", "").split(",")
        if x
    ]
