from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# 🔑 اطلاعات ربات
TOKEN = "8236535117:AAGXLZyB9_AE_e-6vS9jqlKito_dX6fJMHI"
OWNER_ID = 6726103082  # فقط خودت پیام تست رو می‌گیری

# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام ارباب! ربات با موفقیت روی Render بالا اومد 🚀")

# بعد از بالا اومدن ربات، پیام تست ارسال می‌کنه
async def send_test_message(application: Application):
    await application.bot.send_message(chat_id=OWNER_ID, text="ربات روشن شد ✅")

def main():
    app = Application.builder().token(TOKEN).build()

    # اضافه کردن دستور /start
    app.add_handler(CommandHandler("start", start))

    # پیام تست
    app.post_init = send_test_message

    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
