
from telegram.ext import CommandHandler


# '/start' command
def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id, text="test the bot for now!")


start_handler = CommandHandler('start', start)
