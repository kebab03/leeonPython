from selenium import webdriver

#parzialmente OK

class recom():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='C:/Users/leeon/Desktop/chromedriver_win32/chromedriver.exe')

    def recom_info(self):
        self.driver.get(url="https://www.imdb.com/chart/moviemeter/?ref=nv_mv_mpm")
        select = self.driver.find_element_by_xpath('//*[@id="lister-sort-by-options"]')
        select.click()
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

# bot = recom()
# bot.recom_info()