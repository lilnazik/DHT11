import telebot, os
from telebot import types

bot = telebot.TeleBot("659141457:AAEf6Qk7v09q9HWffg8qzBX8Aqd27YSx3pk")
chat_id = 638027434
while True:
    try:
        @bot.message_handler(commands=['start'])
        def send_welcome(message):
            bot.send_message(chat_id, "да привет  я готов")
        @bot.message_handler(content_types=['text'])
        def send_graph(message):
            bot.send_message(chat_id, "Всьо чекаю")
            while True:
                try:
                    sti = open('temp.png', 'rb')
                    bot.send_photo(chat_id, sti)
                    sti = open('hum.png', 'rb')
                    bot.send_photo(chat_id, sti)
                    os.system("rm temp.png")
                    os.system("hum.png.png")
                except:
                    pass
        bot.polling()
    except:
        pass
