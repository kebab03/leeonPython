import speech_recognition as sr
import pyttsx3 as p
from web_automation import *
r = sr.Recognizer()
engine = p.init()
engine.say("hello"
        )
engine.runAndWait()
with sr.Microphone() as source:
    engine.say("Hello , how are you doing?")
    text = r.listen(source)
    try:
        recognised_text =r.recognize_google(text)
        print(recognised_text)
    except sr.UnknownValueError:
        print("")
    except sr.RequestError as  e:
        print("")
