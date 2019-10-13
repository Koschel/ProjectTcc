# -*- coding: utf-8 -*-

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('Chaler', storage_adapter='chatterbot.storage.SQLStorageAdapter',
              logic_adapters=['chatterbot.logic.MathematicalEvaluation',
                              'chatterbot.logic.BestMatch'],
              database_uri='sqlite:///database.sqlite3')

conv = ['Olá',
        'Oi',
        'Qual e o seu nome?',
        'Meu nome é Charler',
        'O que você gosta de fazer?',
        'Gosto de jogar WoW',
        ]

trainer = ListTrainer(bot)

trainer.train(conv)

while True:
    user_input = input('Você: ')
    bot_response = bot.get_response(user_input)
    print('Bot: ', bot_response)
