from pyrogram import Client

from config import Config
from handlers import load_handlers

app = Client(
    "MusicBot",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN
)

load_handlers(app)

app.run()
