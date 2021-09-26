import os
import telebot
import datetime
from request_test import requester
from dotenv import load_dotenv
from request_txt_test import flight_checker

"""
This is the test file for the main loop for the telegram bot program
"""
load_dotenv()


API_KEY = os.getenv("API_KEY_TELEG")
APP_ID_FINAVIA = os.getenv("APP_ID_FINAVIA")
APP_KEY_FINAVIA = os.getenv("APP_KEY_FINAVIA")

bot = telebot.TeleBot(API_KEY)

commands_list = ["/Greet", "/Ville", "/Date", "/Flights"]


def looper(list):
    re = ""
    for item in list:
        re += item + "\n"
    return re


def get_time():
    re = datetime.date.today()
    return re


@bot.message_handler(commands=["Commands"])
def commands(message):
    com = looper(commands_list)
    bot.send_message(message.chat.id, com)


@bot.message_handler(commands=["Greet"])
def greet(message):
    bot.reply_to(message, "Naamanen")


@bot.message_handler(commands=["Ville"])
def name(message):
    bot.reply_to(message, "Mina Ville sina Iiro")


@bot.message_handler(commands=["Date"])
def time(message):
    current_time = get_time()
    bot.reply_to(message, f"Current date is: {current_time}")


@bot.message_handler(commands=["Flights"])
# Flight tester
def time(message):
    bot.send_message(
        message.chat.id, f"Flights:\n {requester(APP_ID_FINAVIA, APP_KEY_FINAVIA)}"
    )


bot.polling()
