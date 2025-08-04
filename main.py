from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters

BOT_TOKEN = "8014831384:AAGKq6euYJFYKQ3y988jbmbMdNUVzrKv_Kw"

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 হ্যালো! আমি একটি ইনফো বট। /help টাইপ করে ফিচার দেখুন।")

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🧠 বট কমান্ড:\n"
        "/start - বট চালু করুন\n"
        "/help - ফিচার তালিকা\n"
        "/myinfo - আপনার তথ্য\n"
        "/ping - বট অনলাইনে আছে কি না\n"
        "/about - বট সম্পর্কে\n"
        "/id - ইউজার বা মেসেজ আইডি"
    )

# /myinfo command
async def myinfo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    info = f"👤 নাম: {user.full_name}\n🆔 ইউজার আইডি: {user.id}\n🔗 ইউজারনেম: @{user.username or 'নেই'}"
    await update.message.reply_text(info)

# /ping command
async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ অনলাইন আছি ভাই!")

# /about command
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 এই বট বানানো হয়েছে তথ্য দেওয়ার জন্য। Made by @yourusername.")

# /id command — Reply message or own ID
async def get_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.reply_to_message:
        user = update.message.reply_to_message.from_user
        await update.message.reply_text(f"🆔 রিপ্লাই ইউজারের আইডি: {user.id}")
    else:
        await update.message.reply_text(f"🆔 আপনার আইডি: {update.effective_user.id}")

# Bot setup
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("myinfo", myinfo))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("about", about))
app.add_handler(CommandHandler("id", get_id))

print("✅ Bot running...")
app.run_polling()