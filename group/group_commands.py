import os
import re
from helpers.status_change import extract_status_change
from datetime import datetime
import logging


from telegram.ext import CallbackContext
from telegram import (ParseMode, InlineKeyboardButton,
                      InlineKeyboardMarkup, Update, Chat)


logger = logging.getLogger(__name__)


def validate_decotator(func):
    def valid_groups(*args, **kwargs):
        update = args[0]
        chat = update.effective_chat
        if chat.type not in [Chat.GROUP, Chat.SUPERGROUP]:
            return
        if not any([id == str(chat.id) for id in os.getenv('GROUP_IDS').split(",")]):
            return
        return func(*args, **kwargs)
    return valid_groups


# User text in group
@validate_decotator
def memeber_chat_inline_keyboard(update: Update, context: CallbackContext) -> None:
    """Handle the inline query."""
    # TODO:
    # Add like function
    # Add dislike function
    # Add user to database
    try:
        chech_for_number = re.search(r'\d+', update.message.text)
        if not chech_for_number:
            return
        keyboard = [
            [
                InlineKeyboardButton("👍 44", callback_data='1'),
                InlineKeyboardButton("👎 5", callback_data='2'),
            ],
            [InlineKeyboardButton(
                "user Details", url=f'https://telegram.me/{os.getenv("BOT_USERNAME")}?start={update.message.from_user.id}')],
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text('Please choose:', reply_markup=reply_markup)
    except:
        return


# Welcaome message
@validate_decotator
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
        added_by = "" if member_name == cause_name else f"\nدعوت شده به گروه توسط: {cause_name}."
        user_name = update.chat_member.new_chat_member.user.username
        update.effective_chat.send_message(
            "\u200c"
            f"کاربر {member_name} به گروه تبادل ارز هلند خوش آمدید."
            f"{added_by}"
            f"\n{'نام کاربری: ' + user_name if user_name else ''}"
            f"\nتاریخ عضویت: {now.strftime('%d/%m/%Y %H:%M')}"
            f"\n لطفا در اولین فرصت با <a href='https://t.me/c/1331406275/1876'>کلیک اینجا</a> قوانین گروه را با دقت مطالعه بفرمائید.",
            parse_mode=ParseMode.HTML,
        )
    # Leave the group message
    # elif was_member and not is_member:
    #     update.effective_chat.send_message(
    #         f"{member_name} is no longer with us. Thanks a lot, {cause_name} ...",
    #         parse_mode=ParseMode.HTML,
    #     )
