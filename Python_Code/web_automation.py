from selenium import webdriver
#c'è un piccolo erroe non riesce a cliccare sul video


class music():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/leeon/Desktop/chromedriver_win32/chromedriver.exe')

    def play(self,name):
        self.name = name
        self.driver.get(url="https://www.youtube.com/results?search_query="+name)
        video = self.driver.find_element_by_xpath('//*[@id="img"]')
        #video = self.driver.find_element_by_xpath('//*[@id="dimissable"]')
        video.click() #//*[@id="img"]
        # search.send_keys(query)
        #
        # enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        # enter.click()
        #
        #
        # info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[2]')
        # readable_text = info.text
        # engine = p.init()
        # engine.say(readable_text)
        # engine.runAndWait()
        #
        #
#
# bot = music()
# bot.play("no women no cry")
# #l'argomento di questa funzione viene preso da speech reconnation  ovvero Jarves
# bot.play("edureka automation