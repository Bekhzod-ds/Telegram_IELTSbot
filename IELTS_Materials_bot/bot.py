import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from telegram.ext import Application

BOT_TOKEN = os.getenv("BOT_TOKEN")
APP_URL = os.getenv("APP_URL")  # e.g. https://your-app-name.onrender.com

PDF_LINK = "https://drive.google.com/uc?export=download&id=1Z14DAxbm0fCQi_CTp_ztmSCgk0SHez3a"
AUDIO_LINK = "https://drive.google.com/uc?export=download&id=12YGPz3FnccmS4fgSCy6aK-ZPrZqTX5G3"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome to IELTS Prep Materials Bot!\n\nUse /get_test to receive a sample IELTS test with audio.")

async def get_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📤 Sending your IELTS mock test...")
    await update.message.reply_document(document=PDF_LINK, filename="IELTS_Mock_Test.pdf")
    await update.message.reply_audio(audio=AUDIO_LINK, filename="IELTS_Listen_Test.mp3")

if __name__ == "__main__":
    application = Application.builder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("get_test", get_test))

    # Set webhook
    PORT = int(os.environ.get("PORT", 8443))
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=BOT_TOKEN,
        webhook_url=f"{APP_URL}/{BOT_TOKEN}",
    )
