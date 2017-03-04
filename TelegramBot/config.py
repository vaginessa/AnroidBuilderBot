#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import telebot

token = 'token'

bot = telebot.TeleBot(token)

hideBoard = telebot.types.ReplyKeyboardRemove()  # if sent as reply_markup, will hide the keyboard
