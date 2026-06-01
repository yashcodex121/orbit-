from pyrogram import filters

async def help_handler(client, message):
    await message.reply_text(
        "Send YouTube URL"
    )

def register(app):
    app.on_message(
        filters.command("help")
    )(help_handler)
