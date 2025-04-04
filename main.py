import os
import logging
from telegram.ext import Application, CommandHandler, ContextTypes
from telegram import Update

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота
TOKEN = os.getenv('TELEGRAM_TOKEN')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот для оценки устройств.')

def main():
    logger.info("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    logger.info("Bot started")
    app.run_polling()

if __name__ == '__main__':
    main()
