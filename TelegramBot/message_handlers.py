#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
from config import *
from sgetters import *


@bot.message_handler(commands=["start"])
def command_start(message: types.Message):
    user = get_user(message)
    print(message.from_user)
    text = "Привет, " + user.get("first_name") + '!\n'
    text += "Присылай мне ссылку на репозиторий 😏"

    bot.send_message(message.chat.id, text, reply_markup=main_menu)


@bot.message_handler(func=lambda message: message.text == "Мои репозитории")
def show_repos_handler(message: types.Message):
    user = get_user(message)
    repos = user.get('repos')
    if repos is None:
        bot.send_message(message.chat.id, "У Вас нет активных репозиториев")
        return

    text = "Ваши репозитории: " + ', '.join(repos)
    bot.send_message(message.chat.id, text)


@bot.message_handler(func=lambda message: message.text == "Добавить репозиторий")
def add_repo_handler(message: types.Message):
    users.update({'id': message.from_user.id},
                 {'$set': {'action': message.text}})

    bot.send_message(message.chat.id, "Введите название репозитория: ")


@bot.message_handler(func=lambda m: True)
def any_message(message: types.Message):
    user = get_user(message)
    if user.get('action') == "Добавить репозиторий":
        add_repo(message)
        bot.send_message(message.chat.id, "Репозиторий успешно добавлен")
        return

    # if re.match(pattern, message.text):
    bot.send_message(message.chat.id, "Ok!")
    file = open('telegram.apk', 'rb')
    print("begin")
    bot.send_document(message.chat.id, file, timeout=3600)
    print('end')
    # else:
    #     bot.send_message(message.chat.id, "Wrong link!")
