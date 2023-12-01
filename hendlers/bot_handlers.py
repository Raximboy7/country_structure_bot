from telebot.types import Message, ReplyKeyboardRemove
from countryinfo import CountryInfo

from  loader import  bot
from keyboards import start_btn

@bot.message_handler(func=lambda message:message.text == 'Country info')
def reaction_country(message: Message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, "Qaysi mamlakat haqida malumot olishni istaysiz?", reply_markup=ReplyKeyboardRemove())
    bot.register_next_step_handler(msg, get_info)



def get_info(message:Message):
    chat_id = message.chat.id
    try:
        country = message.text
        info = CountryInfo(country).info()
        capital = info['capital']
        population = info['population']
        area = info['area']
        region = info['region']
        bot.send_message(chat_id, f"""{country.capitalize()} ma'lumotlari:
Poytaxti: {capital}
Maydon kengligi: {area}
Aholi soni: {population}
Mintaqa: {region}""", reply_markup=start_btn())
    except:
        bot.send_message(chat_id, "Mamlakat nomi xato kritilgan!")