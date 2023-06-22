import os
# import sqlite3
#
# import datetime
# from datetime import date
import time
from main_functions import show_timeline
import telebot
from telebot import types
from dotenv import load_dotenv

load_dotenv()
# token = os.getenv('TELEGRAM_MEETUP_BOT_API_TOKEN')
token = '5997099999:AAExP16I4FUFWZfn3NLWhF4yUI00e-pQi3k'
bot = telebot.TeleBot(token)
conference = [('знакомство', '10:00 - 11:00', 'Иван'), ('прощание', '11:00 - 12:00', 'Юрий')]
# conn = sqlite3.connect('conference/db.sqlite3', check_same_thread=False)
# cursor = conn.cursor()
#
questions = ['вопрос 1', 'вопрос 2', 'вопрос 3']
speakers = []
user = 0


def my_question(message):
    question = message.text
    questions.append(question)


def send_questions(questions):
    for question in questions:
        return question


# def bd_table_val(id: int, time: str, theme: str, name: str, t_name: str, wait_time: bool):
#     cursor.execute('INSERT INTO conference(time, theme, name, t_name, wait_time) VALUES (?,?,?,?,?)',
#                    (params[-2], params[3], params[0], params[1], params[2]))
#     conn.commit()

@bot.message_handler(commands=['start'])
def start(message):

    if message.from_user.username == 'AbRamS0404':
        markup = types.InlineKeyboardMarkup(row_width=1)
        timeline = types.InlineKeyboardButton('График выступлений', callback_data='timeline')
        markup.add(timeline)
        bot.send_message(message.chat.id, '\nпосмотрим расписание?\n', reply_markup=markup)

    elif message.from_user.username == 'Konstantin_Derienko':  #in speakers: # добавить сравнение времени спикера и текущего времени
        markup = types.InlineKeyboardMarkup(row_width=1)
        questions = types.InlineKeyboardButton('Вопросы слушателей', callback_data='questions')
        timeline = types.InlineKeyboardButton('График выступлений', callback_data='timeline')
        ask_question = types.InlineKeyboardButton('Задать вопрос', callback_data='ask_question')
        about_bot = types.InlineKeyboardButton('Что я могу', callback_data='about')
        markup.add(questions, timeline, ask_question, about_bot)

        bot.send_message(message.chat.id, '\nвыбери нужный пункт', reply_markup=markup)

    else:
        markup = types.InlineKeyboardMarkup(row_width=1)
        timeline = types.InlineKeyboardButton('График выступлений', callback_data='timeline')
        ask_question = types.InlineKeyboardButton('Задать вопрос', callback_data='ask_question')
        about_bot = types.InlineKeyboardButton('Что я могу', callback_data='about')
        markup.add(timeline, ask_question, about_bot)

        bot.send_message(message.chat.id, '\nвыбери нужный пункт', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):

    if call.data == 'about':
        text = 'Я расскажу какие ожидаются выступления, а еще через меня можно задать вопрос спикеру!'
        markup = types.InlineKeyboardMarkup(row_width=1)
        home = types.InlineKeyboardButton('Домой', callback_data='home')
        markup.add(home)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f'\n{text}',
                              parse_mode='Markdown', reply_markup=markup)

    elif call.data == 'timeline':  # тут будет график из БД
        markup = types.InlineKeyboardMarkup(row_width=1)
        home = types.InlineKeyboardButton('Домой', callback_data='home')
        markup.add(home)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f'\n{show_timeline(conference)}',
                              reply_markup=markup)

    elif call.data == 'ask_question':  # будет сохранять вопрос спикеру в БД
        markup = types.InlineKeyboardMarkup(row_width=2)

        ask = types.InlineKeyboardButton('Спросить', callback_data='ask')
        item5 = types.InlineKeyboardButton('Домой', callback_data='home')
        markup.add(ask, item5)
        sent = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                                     text='\nЗадай свой вопрос\n\n',
                                     reply_markup=markup)
        bot.register_next_step_handler(sent, my_question)

    elif call.data == 'ask':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text='\nСпасибо за вопрос\n\n')

    elif call.data == 'questions':  # будет брать вопросы из БД для конкретного спикера
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id,
                              text=f'\n{send_questions(questions)}\n')

    elif call.data == 'home':
        bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
        start(call.message)


def main():
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as error:
            print(error)
            time.sleep(5)


if __name__ == '__main__':
    main()
