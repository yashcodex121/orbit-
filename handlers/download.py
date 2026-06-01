from pyrogram import filters

from core.downloader import YTDLPManager

async def download_handler(client, message):

    if len(message.command) < 2:
        return await message.reply_text(
            "Usage:\n/download link"
        )

    url = message.command[1]

    track = await YTDLPManager.extract_info(url)

    await message.reply_text(
        f"🎵 {track.title}"
    )

def register(app):
    app.on_message(
        filters.command("download")
    )(download_handler)
