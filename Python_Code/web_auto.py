from selenium import webdriver
import  pyttsx3 as p
#OK

class info():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/leeon/Desktop/chromedriver_win32/chromedriver.exe')

    def get_info(self,query):
        self.query = query
        self.driver.get(url="https://www.wikipedia.org/")
        search = self.driver.find_element_by_xpath('//*[@id="searchInput"]')
        search.click()
        search.send_keys(query)
# https://chercher.tech/python/relative-xpath-selenium-python.php
        enter = self.driver.find_element_by_xpath('//*[@id="search-form"]/fieldset/button')
        enter.click()


        info = self.driver.find_element_by_xpath('//*[@id="mw-content-text"]/div/p[2]')
        readable_text = info.text
        engine = p.init()
        engine.say(readable_text)
        engine.runAndWait()



# bot = info()
# bot.get_info("liberty bell")