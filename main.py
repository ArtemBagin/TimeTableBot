from timetable import TimeTable

import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from environs import Env

env = Env()
env.read_env()

bot = telebot.TeleBot(env.str("TOKEN"))
tb = TimeTable()


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton("Расписание на сегодня"),
        KeyboardButton("Расписание на неделю")
    )
    bot.send_message(message.chat.id, 'Привет, этот бот предназначен для '
                                      'просмотра расписания группы ДЭ-117\n'
                                      'Выберите действие кнопкой ниже.',
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def timetable_handler(message):
    if message.text == "Расписание на сегодня":
        bot.send_message(message.chat.id, tb.get_today_timedata())
    elif message.text == 'Расписание на неделю':
        bot.send_message(message.chat.id, tb.get_week_timedata())


bot.infinity_polling()

