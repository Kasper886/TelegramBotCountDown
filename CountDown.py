# -*- coding: utf-8 -*-
import telebot
import datetime
from time import sleep
from threading import Thread

bot = telebot.TeleBot("YourBotAPI")


@bot.message_handler(commands=['start'])
def thread_main(message):
    Thread(target=timer, args=(message,)).start()
    #Thread(target=counter, args=(message,)).start()

def timer(message):
    msg = bot.send_message(chat_id=message.chat.id, text='Timer starts')
    sleep(1)
    msg_id = msg.message_id

    start = datetime.datetime.now()
    finish = datetime.datetime(2023,2,26,21,59,59)
    time_s = finish - start
    time_s = int(time_s.total_seconds())
    for t in range(time_s, 0, -5):

        #days = datetime.datetime.fromtimestamp(t).strftime('%d')
        hours = datetime.datetime.fromtimestamp(t).strftime('%H')
        mins = datetime.datetime.fromtimestamp(t).strftime('%M')
        secs = datetime.datetime.fromtimestamp(t).strftime('%S')
        bot.edit_message_text(chat_id=message.chat.id,  message_id=msg_id, text=f'До окончания скидки на создание сайта Авенирычу осталось: \n00 дн. {hours} ч. {mins} мин. {secs} сек.')
        sleep(5)

    bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id, text='Время вышло!')

"""
def counter(message):
    msg = bot.send_message(chat_id=message.chat.id, text='Count start')
    sleep(1)
    msg_id = msg.message_id
    count = 15
    for c in range(count):
        bot.edit_message_text(chat_id=message.chat.id,  message_id=msg_id, text=f'Count - {c}')
        sleep(1)
    bot.edit_message_text(chat_id=message.chat.id, message_id=msg_id, text='Count End')
"""

if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(e)
