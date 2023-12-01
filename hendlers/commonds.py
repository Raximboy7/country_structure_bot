from  telebot.types import Message

from keyboards import start_btn

from loader import bot

@bot.message_handler(commands=['start'])
def reaction_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alekom, {message.from_user.full_name}", reply_markup=start_btn())


