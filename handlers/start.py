from pyrogram import filters

async def start_handler(client, message):
    await message.reply_text(
        "🎵 Music Bot Started"
    )

def register(app):
    app.on_message(
        filters.command("start")
    )(start_handler)
