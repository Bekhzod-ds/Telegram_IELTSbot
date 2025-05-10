import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from telegram.ext import Application

BOT_TOKEN = os.getenv("BOT_TOKEN")

PDF_LINK = "https://drive.google.com/uc?export=download&id=1Z14DAxbm0fCQi_CTp_ztmSCgk0SHez3a"
AUDIO_LINK = "https://drive.google.com/uc?export=download&id=12YGPz3FnccmS4fgSCy6aK-ZPrZqTX5G3"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Welcome to IELTS Prep Materials Bot!\n\n"
        "Use /get_test to receive a sample IELTS test with audio."
    )

async def get_test(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📤 Sending your IELTS mock test...")
    await update.message.reply_document(document=PDF_LINK, filename="IELTS_Mock_Test.pdf")
    await update.message.reply_audio(audio=AUDIO_LINK, filename="IELTS_Listen_Test.mp3")

if __name__ == "__main__":
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("get_test", get_test))

    # Use Flask to ensure the app runs on Render
    from flask import Flask
    app_flask = Flask(__name__)

    @app_flask.route("/")
    def webhook():
        return "Bot is running!"

    app_flask.wsgi_app = DispatcherMiddleware(app_flask.wsgi_app, {
        '/': app.run_polling
    })

    # Render expects to bind to a port
    port = int(os.environ.get("PORT", 5000))
    app_flask.run(host="0.0.0.0", port=port)
