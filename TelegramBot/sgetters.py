#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from telebot import types
from config import *


def new_user(message: types.Message):
    users.save({'id': message.from_user.id, 'first_name': message.from_user.first_name,
                'last_name': message.from_user.last_name, 'username': message.from_user.username,
                'time': datetime.datetime.now().strftime("%H %M %S"),
                'repos': None, 'action': None})


def get_user(message):
    user = users.find_one({'id': message.from_user.id})
    if user is None:
        new_user(message)
        user = users.find_one({'id': message.from_user.id})

    users.update({'id': message.from_user.id},
                 {'$set': {'time': datetime.datetime.now().strftime("%H %M %S")}})

    return user


def add_repo(message: types.Message):
    user = get_user(message)
    repos = user.get('repos')

    if repos is None:
        repos = []

    repos.append(message.text)

    users.update({'id': message.from_user.id},
                 {'$set': {'repos': repos,
                           'action': None}})
