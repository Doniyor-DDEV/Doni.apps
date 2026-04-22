from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "8561546560:AAEPF75cJgJRcHVYEXoWpjeo4y6LdbeuG6k"
WEB_APP_URL = "https://doniyor-ddev.github.io/Doni.apps/" # Oxirida index.html bo'lishi shart emas

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 O'yinlar Menyusi", web_app=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Salom! 🕹 Game Hub botiga xush kelibsiz!\n\n"
        "O'yinlarni o'ynash uchun quyidagi tugmani bosing:",
        reply_markup=reply_markup
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

if __name__ == '__main__':
    print("Bot ishga tushdi...")
    app.run_polling()