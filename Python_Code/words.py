import  pyttsx3 as p
engine = p.init()
meanings= {"certification":"the action of providing",
           "Programming":"the process of writing",
           "skill":"the ability to do something well",
           "automation":"the use of automatic equipment",
           "robot":"a machine that can do human work"
}

translations = {"certification":"certificazione",
                "Programming":"Programmazion",
                "skill":"ablita",
                "automation":"automazione",
                "robot":"automi"}
def mean(name):
    if name in meanings:
       res = meanings[name]

       engine.say("the meanings of"+name+ "is that"+res)

       engine.runAndWait()


def translate(name):
    if name in translations:
        res = translations[name]  #[id ]  la la parte di dictonary dato la parola chia
        engine.say("the word translates to " + res +"in spanish")
        engine.runAndWait()
# mean("certification")
# translate("certification")
#bot = info()
#bot.get_info("liberty bell")