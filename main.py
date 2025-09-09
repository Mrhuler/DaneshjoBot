from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# تنظیمات ارباب 👑
TOKEN = "8236535117:AAGXLZyB9_AE_e-6vS9jqlKito_dX6fJMHI"
ADMIN_ID = 6726103082

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID:
        await update.message.reply_text("شما مجاز به استفاده از این ربات نیستید ❌")
        return
    await update.message.reply_text("سلام ارباب 👑، بات آنلاین شد و آماده‌ست!")

# پیام عادی
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id == ADMIN_ID:
        await update.message.reply_text(f"پیام دریافت شد: {update.message.text}")
    else:
        await update.message.reply_text("دسترسی نداری ❌")

def main():
    # ساخت اپلیکیشن
    app = Application.builder().token(TOKEN).build()

    # دستورها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # اجرای ربات
    app.run_polling()

if __name__ == "__main__":
    main()
