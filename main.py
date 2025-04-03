import os
from telegram.ext import Application, CommandHandler
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
PORT = int(os.getenv('PORT', 8443))

async def start(update, context):
    await update.message.reply_text('Привет! Я ваш бот.')

def main():
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    
    # Railway требует веб-хук вместо polling
    application.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        webhook_url=os.getenv('WEBHOOK_URL')
    )

if __name__ == '__main__':
    main()