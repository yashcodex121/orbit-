import yt_dlp
import asyncio

from core.models import TrackInfo


class YTDLPManager:

    @staticmethod
    async def extract_info(url):

        def sync():
            with yt_dlp.YoutubeDL({"quiet": True}) as ydl:
                return ydl.extract_info(url, download=False)

        data = await asyncio.get_event_loop().run_in_executor(
            None,
            sync
        )

        return TrackInfo(
            url=url,
            title=data.get("title"),
            artist=data.get("uploader"),
            duration=data.get("duration", 0),
            thumbnail=data.get("thumbnail", "")
        )
