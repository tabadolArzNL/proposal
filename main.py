import os
import logging

from telegram.ext import (
    Updater,
    ChatMemberHandler,
    Filters,
    MessageHandler
)
from telegram import Update
from dotenv import load_dotenv

# import the commands
from pm import pm_commands
from group import group_commands


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Start the bot."""
    # Load all env var from '.env' file
    load_dotenv()
    # Create the Updater and pass it your bot's token.
    updater = Updater(token=os.getenv('TOKEN'),
                      use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher
    # # # # # # # #
    # All handlers
    # # # # # # # #
    dispatcher.add_handler(pm_commands.start_handler)
    dispatcher.add_handler(ChatMemberHandler(
        group_commands.greet_chat_members, ChatMemberHandler.CHAT_MEMBER))
    # dispatcher.add_handler(MessageHandler(
    #     Filters.text & ~Filters.command, group_commands.memeber_chat_inline_keyboard))

    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                        level=logging.INFO)

    updater.start_polling(allowed_updates=Update.ALL_TYPES)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    updater.idle()


if __name__ == "__main__":
    main()
