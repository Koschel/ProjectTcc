# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import speech_recognition as sr
import pyttsx3 as pytts


bot = ChatBot('Charle')
speak = pytts.init('sapi5')

conv = ['Olá',
        'Oi',
        'Qual e o seu nome?',
        'Meu nome é Charler',
        'O que você gosta de fazer?']

trainer = ListTrainer(bot)

trainer.train(conv)

def Speak(text):
    speak.say(text)
    speak.runAndWait()

def recognize():
    print('Escutando...')
    rec = sr.Recognizer()
    with sr.Microphone() as mp:
        rec.adjust_for_ambient_noise(mp)

        while True:
            try:
                audio = rec.listen(mp)
                user_input = rec.recognize_google(audio, language="pt")
                print('Você: ', user_input)
                bot_response = bot.get_response(user_input)
                print('Bot:', bot_response)
                Speak(bot_response)
            except sr.UnknownValueError:
                return "Desculpe, não entendi"


speech = recognize()
print(speech)