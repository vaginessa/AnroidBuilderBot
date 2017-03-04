#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import telebot
from telebot import types
import pymongo
import datetime


token = '308090481:AAHisVkkFnX9U7WBvUHXSkZdju409Np-TFI'

bot = telebot.TeleBot(token)

client = pymongo.MongoClient()
db = client.hackabase
users = db.users

hideBoard = telebot.types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard

pattern = "(https?\:\/\/)?github\.com[\w\/]+"

main_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False, selective=True)
main_menu.add('Мои репозитории')
main_menu.row('Добавить репозиторий')
