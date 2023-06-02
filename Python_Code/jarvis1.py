import speech_recognition as sr

from web_auto import *
from web_auto1 import *
from web_automation import *
from recommendations import *
from words import *
from time import sleep

# intial conversation
r1 = sr.Recognizer()
engine = p.init()
engine.say("Hello leeon , how are you doing today?")
engine.runAndWait()
with sr.Microphone() as source:
    r1.adjust_for_ambient_noise(source)
    # print("how are you doing today?")
    print("5 ms per dire  hello  oppure how are you 1 sola votla")
    sleep(5)
    print("ora ")

    audio = r1.listen(source)
    try:
        text = r1.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as  e:
        print("")

        # chiede istruzioni
    engine.say("what like me to do?")
    engine.runAndWait()
    print("what do you want : tra ,meaning,translate,recommendation,information ,music,review")
    # ginvin instruction     try:
    r2 = sr.Recognizer()
    with sr.Microphone() as source:
        # print("how are you doing today?")
        r2.adjust_for_ambient_noise(source)
        audio = r2.listen(source)
        try:
            instruction = r2.recognize_google(audio)  # converte l'audio in text
            print("quello ho detto dopo how r yu:", text)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as  e:
            print("")

# getting info da wiki pedi
r3 = sr.Recognizer()
if "information" in instruction:  # se non sbaglio la ricerca si fa string pe rstringa e nn per char per char
    engine.say("info about what you wando ?")
    engine.runAndWait()
    with sr.Microphone() as source1:
        print("5 ms per dire  info che vuoi")
        sleep(5)
        print("ora ")
        audio2 = r3.listen(source1)
        print("audio2:" ,audio2)
        try:
            information = r3.recognize_google(audio2)
            print("information:", information)
            bot = info()  # viene da web_auto
            bot.get_info(information)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as  e:
            print("")

# movie rating revie
r4 = sr.Recognizer()
if "review" in instruction:  # movie review
    engine.say(" what is the name of movie ")
    engine.runAndWait()
    with sr.Microphone() as source2:
        audio3 = r4.listen(source2)
        try:
            rating = r4.recognize_google(audio3)
            bot = Movie()  # web_auto1   cui chiamo la classe
            bot.movie_review(rating)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as  e:
            print("")

# play music
r5 = sr.Recognizer()
if "music" in instruction:  # da weutomatio
    engine.say("which artist should i play?")
    engine.runAndWait()
    with sr.Microphone() as source3:
        audio4 = r5.listen(source3)
        try:
            video = r5.recognize_google(audio4)
            bot = music()
            bot.play(video)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as  e:
            print("")

# movie recomention
if "recommendation " in instruction:
    engine.say("Here are list of movies you can chose to watch from ")
    engine.runAndWait()
    bot = recom()  # da recommendation module
    bot.recom_info()

# getting meaning of words
r6 = sr.Recognizer()
if "meaning" in instruction:
    engine.say("which word sire?")
    engine.runAndWait()
    with sr.Microphone() as source4:
        audio5 = r6.listen(source4)
        try:  # da module word
            word = r6.recognize_google(audio5)
            # bot = word()
            mean(word)  ################ ho modificato io
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as  e:
            print("")
# getting the translation in spanish OK
r7 = sr.Recognizer()  # da modulo rd
if "translate" in instruction:
    engine.say("what do you want to translate sire?")
    engine.runAndWait()
    with sr.Microphone() as source5:
        audio6 = r7.listen(source5)
        try:
            word1 = r7.recognize_google(audio6)
            translate(word1)
        except sr.UnknownValueError:
            print("")
        except sr.RequestError as  e:
            print("")
            # tra questo print posso andare a vedere dal sito le eccesioni