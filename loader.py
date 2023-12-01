from telebot import TeleBot
from telebot.types import BotCommand
from config import TOKEN

bot = TeleBot(TOKEN)

bot.set_my_commands(commands=[
    BotCommand('start', 'botni ishga tushurish burugi!'),
    BotCommand('help', 'hatolarni tuzatish buyrugi!')
])