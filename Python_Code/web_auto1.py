from selenium import webdriver
import  pyttsx3 as p
#  OK

class Movie():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/leeon/Desktop/chromedriver_win32/chromedriver.exe')

    def movie_review(self,name):
        self.driver.get(url="https://www.google.com")
        search = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
        search.click()
        search.send_keys(name + "movie review")
        submit = self.driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[2]/div[2]/div[2]/center/input[1]')
        submit.click()

        # enter = self.driver.find_element_by_xpath()
        # enter.click()
        #
        #
        # info = self.driver.find_element_by_xpath()
        # readable_text = info.text
        # engine = p.init()
        # engine.say(readable_text)
        # engine.runAndWait()


#
# bot = Movie()
# bot.movie_review("Pursuit of happines ")