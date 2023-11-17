import logging

from telegram import Update
from telegram.ext import (filters,
                          MessageHandler,
                          ApplicationBuilder,
                          CommandHandler,
                          ContextTypes)


from config import token, pingvin_chat_id


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Привет! Я Бот!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=pingvin_chat_id,
                                   text=update.message.text)


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Sorry, I didn't understand that command.")


if __name__ == '__main__':

    application = ApplicationBuilder().token(token).build()
    start_handler = CommandHandler('start', start)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)

    unknown_handler = MessageHandler(filters.COMMAND, unknown)

    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(unknown_handler)

    application.run_polling()
