# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


import speech_recognition as sr
import pyttsx3 as pytts


bot = ChatBot('Charle')
speak = pytts.init('sapi5')

conv = open('chatterbot_HTML.txt', 'r', encoding='utf-8').readlines()
trainer = ListTrainer(bot)
trainer.train(conv)

#trainer.train(conv)

def Speak(text):
    speak.say(text)
    speak.runAndWait()

def recognize():
    msgInicial = 'Para verificar quais tópicos de estudo você possui fale o comando "Iniciar estudos", para parar o fale o comando Parar, O que você deseja fazer ?'
    print('Charle' + msgInicial)
    Speak(msgInicial)
    rec = sr.Recognizer()
    with sr.Microphone() as mp:
        rec.adjust_for_ambient_noise(mp)

        while True:
            try:
                audio = rec.listen(mp)
                user_input = rec.recognize_google(audio, language="pt")
                print('Você: ', user_input)
                if user_input == 'Nao' or user_input == 'nao' or user_input == 'não' or user_input == 'Não' or user_input == 'n' or user_input == 'nada' or user_input == 'Nada' or user_input == 'Parar' or user_input== 'parar':
                    mgsSair = 'Acabamos por aqui, até logo'
                    print(mgsSair)
                    Speak(mgsSair)
                    break
                bot_response = bot.get_response(user_input)
                print('Charle:', bot_response)
                Speak(bot_response)

            except sr.UnknownValueError:
                erro = "Desculpe, não entendi"
                print(erro)
                Speak(erro)


speech = recognize()
print(speech)