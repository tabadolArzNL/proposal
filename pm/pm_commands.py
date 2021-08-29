
from telegram.ext import CommandHandler
from telegram import Chat


# '/start' command
def start(update, context):
    msg = update.message.text.split(" ")
    chat = update.effective_chat
    text = ""
    if chat.type == Chat.PRIVATE:
        if len(msg) > 1:
            # TODO: send the user deatils back
            text = "[Future] Will check database for that user and will send the deatils here"
        else:
            text = "Private chat with bot text!"

    elif chat.type in [Chat.GROUP, Chat.SUPERGROUP]:
        text = "Type start on group"

    context.bot.send_message(
        chat_id=update.effective_chat.id, text=text)


start_handler = CommandHandler('start', start)
