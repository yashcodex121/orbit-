import aiohttp
import os

class ThumbnailHandler:

    @staticmethod
    async def fetch(url, path):

        file = os.path.join(path, "thumb.jpg")

        async with aiohttp.ClientSession() as session:
            async with session.get(url) as r:
                with open(file, "wb") as f:
                    f.write(await r.read())

        return file
