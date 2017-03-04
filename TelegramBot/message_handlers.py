#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from telebot import types
from config import *


@bot.message_handler(commands=["start"])
def command_start(message: types.Message):
    text = "Hi!"
    bot.send_message(message.chat.id, text)
