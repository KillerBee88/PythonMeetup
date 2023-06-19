import logging
import telebot
import os
from dotenv import load_dotenv
from environs import Env
from sql_functions import (
    sql_register_new_user,
    sql_add_new_spiker,
    sql_get_user_data,
    sql_put_user_phone)


logging.basicConfig(filename='bot.log', level=logging.INFO)


env = Env()
env.read_env(override=True)
load_dotenv()
token = os.getenv('TELEGRAM_MEETUP_BOT_API_TOKEN')
bot = telebot.TeleBot(token)