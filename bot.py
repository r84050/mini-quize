import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import json

BOT_TOKEN    = "YOUR_BOT_TOKEN"
MINI_APP_URL = "https://r84050.github.io/mini-quize/"

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [[InlineKeyboardButton("🎯 Play Mini Quize", web_app=WebAppInfo(url=MINI_APP_URL))]]
    await update.message.reply_text(
        f"Hey {user.first_name}! 👋\n\nWelcome to *Mini Quize* 🎯\n\n5 questions • Predict the computer • Score points!\n\nTap below to start 👇",
        parse_mode="Markdown",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

async def web_app_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data     = json.loads(update.message.web_app_data.data)
        correct  = data.get("correct", 0)
        wrong    = data.get("wrong", 0)
        total    = correct + wrong
        accuracy = round((correct / total * 100)) if total > 0 else 0
        emoji    = "🏆" if accuracy >= 80 else "👍" if accuracy >= 50 else "😅"
        await update.message.reply_text(
            f"{emoji} *Quiz Complete!*\n\n✅ Correct: {correct}\n❌ Wrong: {wrong}\n🎯 Accuracy: {accuracy}%",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🔁 Play Again", web_app=WebAppInfo(url=MINI_APP_URL))]])
        )
    except Exception as e:
        logging.error(f"Error: {e}")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data))
    print("✅ Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
