# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

import speech_recognition as sr
import pyttsx3 as pytts


bot = ChatBot('Charle')
speak = pytts.init('sapi5')

conv = ['começar Estudos',
        'tópico um existente: HTML',
        'começar',
        'tópico 1 existente: HTML']

conv = ['topico um',
        'HTML (abreviação para a expressão inglesa HyperText Markup Language, que significa Linguagem de Marcação de Hipertexto) é uma linguagem de marcação utilizada na construção de páginas na Web. Documentos HTML podem ser interpretados por navegadores. A tecnologia é fruto da junção entre os padrões HyTime e SGML HyTime é um padrão para a representação estruturada de hipermídia e conteúdo baseado em tempo. Um documento é visto como um conjunto de eventos concorrentes dependentes de tempo (como áudio, vídeo, etc.), conectados por hiperligações. O padrão é independente de outros padrões de processamento de texto em geral',
        'topico 1',
        'HTML (abreviação para a expressão inglesa HyperText Markup Language, que significa Linguagem de Marcação de Hipertexto) é uma linguagem de marcação utilizada na construção de páginas na Web. Documentos HTML podem ser interpretados por navegadores. A tecnologia é fruto da junção entre os padrões HyTime e SGML HyTime é um padrão para a representação estruturada de hipermídia e conteúdo baseado em tempo. Um documento é visto como um conjunto de eventos concorrentes dependentes de tempo (como áudio, vídeo, etc.), conectados por hiperligações. O padrão é independente de outros padrões de processamento de texto em geral'
        ]

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