import telebot
import requests
import shutil
bot = telebot.TeleBot('5888792736:AAFcpx1gs78w53f4_2J-9gFFAEOnoqapFP0') 
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет! Я бот который может скинуть бота. Хочешь?")
@bot.message_handler(content_types=['text'])
def get_user_text(message):
    user_text=message.text
    if (user_text=="Да") or (user_text=="да"):
        r = requests.get('http://thecatapi.com/api/images/get?format=src')
        url = r.url
        bot.send_photo(message.chat.id, url,)
        bot.send_message(message.chat.id, "Еще кота?")
    elif (user_text=="Нет") or (user_text=="нет"):
        bot.send_message(message.chat.id, "Хорошо, пока!")
bot.polling(non_stop=True)