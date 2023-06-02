import  pyttsx3 as p
engine=p.init()
volume = engine.getProperty("volume")
print(volume)
engine.say("hello"
        )
engine.say("Hello , how are you doing?")
engine.say("what you like me to do?")
engine.runAndwait()
with sr.Microphone() as source:
    text =r.listen(source)
    try:
        reco
