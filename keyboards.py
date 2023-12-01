from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def start_btn():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    key = KeyboardButton('Country info')
    markup.add(key)
    return markup