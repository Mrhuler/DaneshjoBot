from telegram import Update, ReplyKeyboardRemove
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

NAME, CODE, SIGNATURE = range(3)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! لطفاً نام و نام خانوادگی‌تان را وارد کنید:")
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["name"] = update.message.text
    await update.message.reply_text("کد دانشجویی خود را وارد کنید:")
    return CODE

async def get_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data["code"] = update.message.text
    await update.message.reply_text("حالا لطفاً امضای خود را روی کاغذ بکشید و عکسش را ارسال کنید:")
    return SIGNATURE

async def get_signature(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.message.photo:
        await update.message.reply_text("لطفاً عکس امضا را ارسال کنید.")
        return SIGNATURE

    context.user_data["signature"] = update.message.photo[-1].file_id

    admin_id = 6726103082
    bot = context.bot
    await bot.send_message(chat_id=admin_id,
        text=f"فرم جدید:\n\nنام و نام خانوادگی: {context.user_data['name']}\nکد دانشجویی: {context.user_data['code']}")
    await bot.send_photo(chat_id=admin_id, photo=context.user_data["signature"])
    await update.message.reply_text("اطلاعات شما با موفقیت ثبت شد. ممنون 🌹")
    return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("عملیات لغو شد.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END

def main():
    app = Application.builder().token("8236535117:AAGXLZyB9_AE_e-6vS9jqlKito_dX6fJMHI").build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_code)],
            SIGNATURE: [MessageHandler(filters.PHOTO, get_signature)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )
    app.add_handler(conv_handler)
    print("بات آماده و در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
