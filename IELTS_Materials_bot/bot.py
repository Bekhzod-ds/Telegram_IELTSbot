import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

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
    print("🤖 Bot is running...")
    app.run_polling()
