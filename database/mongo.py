from motor.motor_asyncio import AsyncIOMotorClient
from config import Config

mongo = AsyncIOMotorClient(Config.MONGO_URI)

db = mongo[Config.DB_NAME]

file_cache = db.file_cache
downloads = db.downloads
users = db.users
playlists = db.playlists
