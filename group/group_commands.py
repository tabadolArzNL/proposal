import os
import re
from helpers.status_change import extract_status_change
from datetime import datetime
import logging


from telegram.ext import CallbackContext
from telegram import (ParseMode, InlineKeyboardButton,
                      InlineKeyboardMarkup, Update, Chat)


logger = logging.getLogger(__name__)


# User text in group
def memeber_chat_inline_keyboard(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    # TODO:
    # Add like function
    # Add dislike function
    # Add user to database
    chat = update.effective_chat
    chech_for_number = re.search(r'\d+', update.message.text)

    if chat.type not in [Chat.GROUP, Chat.SUPERGROUP] or not chech_for_number:
        return

    keyboard = [
        [
            InlineKeyboardButton("Like this user (👍 44)", callback_data='1'),
            InlineKeyboardButton("Dislike this user (👎 5)", callback_data='2'),
        ],
        [InlineKeyboardButton(
            "See this user Details", url=f'https://telegram.me/{os.getenv("BOT_USERNAME")}?start={update.message.from_user.id}')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Please choose:', reply_markup=reply_markup)


# Welcaome message
def greet_chat_members(update: Update, context: CallbackContext) -> None:
    """Greets new users in chats"""
    result = extract_status_change(update.chat_member)
    if result is None:
        return

    was_member, is_member = result
    cause_name = update.chat_member.from_user.mention_html()
    member_name = update.chat_member.new_chat_member.user.mention_html()

    if not was_member and is_member:
        now = datetime.now()
        added_by = "" if member_name == cause_name else f"\nInvited By: {cause_name}."
        user_name = update.chat_member.new_chat_member.user.username
        update.effective_chat.send_message(
            f"Welcome {member_name}."
            f"{added_by}"
            f"\n{'user_name: ' + user_name if user_name else ''}"
            f"\nJoin date: {now.strftime('%d/%m/%Y %H:%M')}"
            f"\nPlease first read the roles: <a href='https://t.me/c/1331406275/1876'>click here</a>",
            parse_mode=ParseMode.HTML,
        )
    # Leave the group message
    # elif was_member and not is_member:
    #     update.effective_chat.send_message(
    #         f"{member_name} is no longer with us. Thanks a lot, {cause_name} ...",
    #         parse_mode=ParseMode.HTML,
    #     )
