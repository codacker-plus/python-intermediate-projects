# telegram_bot.py
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

def start(update, context):
    """Handle /start command."""
    update.message.reply_text("Hello! I'm a simple Telegram bot. Send me any message!")

def echo(update, context):
    """Echo the user's message."""
    update.message.reply_text(f"You said: {update.message.text}")

def telegram_bot():
    """Main function for Telegram bot."""
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token from BotFather
    TOKEN = 'YOUR_BOT_TOKEN'
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Add handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Start the bot
    updater.start_polling()
    print("Bot is running...")
    updater.idle()

if __name__ == "__main__":
    telegram_bot()
