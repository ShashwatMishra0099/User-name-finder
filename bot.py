from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, UpdateQueue

TOKEN = "7073136015:AAEhuHGqeaEm33aNTtNHYmB8jBisAMQL1oA"

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! I'm your Telegram bot. Use /members to get the list of members with usernames.")

def members(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    members = context.bot.get_chat_members_count(chat_id)
    member_list = context.bot.get_chat_members(chat_id)
    response = "Total Members: {}\n".format(members)
    response += "Members List:\n"
    for member in member_list:
        response += "{} - @{}\n".format(member.user.full_name, member.user.username)
    update.message.reply_text(response)

def main() -> None:
    updater = Updater(TOKEN, use_context=True, update_queue=UpdateQueue())
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("members", members))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
