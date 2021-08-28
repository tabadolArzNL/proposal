import os
import logging
from telegram.ext import Updater
from dotenv import load_dotenv
# import the commands
from pm import pm_commands

# Load all env var from '.env' file
load_dotenv()
# Setup the bot
updater = Updater(token=os.getenv('TOKEN'),
                  use_context=True)
dispatcher = updater.dispatcher
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
# # # # # # # #
# All handlers
# # # # # # # # 
dispatcher.add_handler(pm_commands.start_handler)

updater.start_polling()
