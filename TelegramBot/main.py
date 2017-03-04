#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import telebot
from config import bot
import message_handlers


if __name__ == "__main__":
    bot.remove_webhook()
    bot.polling(none_stop=True)
