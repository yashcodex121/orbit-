import asyncio
import yt_dlp

from core.models import TrackInfo


class YTDLPManager:

    @staticmethod
    async def extract_info(url):

        def sync():

            ydl_opts = {
                "quiet": True,
                "no_warnings": True,
                "extract_flat": False,
                "geo_bypass": True,
                "nocheckcertificate": True,
                "ignoreerrors": False,
                "extractor_args": {
                    "youtube": {
                        "player_client": [
                            "android",
                            "ios",
                            "web"
                        ]
                    }
                }
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                return ydl.extract_info(url, download=False)

        try:
            data = await asyncio.get_running_loop().run_in_executor(
                None,
                sync
            )

            if not data:
                return None

            return TrackInfo(
                url=url,
                title=data.get("title", "Unknown Title"),
                artist=data.get("uploader", "Unknown Artist"),
                duration=data.get("duration", 0),
                thumbnail=data.get("thumbnail", "")
            )

        except yt_dlp.utils.DownloadError as e:
            print(f"YT-DLP Error: {e}")
            return None

        except Exception as e:
            print(f"Extract Error: {e}")
            return None
