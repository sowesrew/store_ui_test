from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageStore:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, element):
        element.click()

    #def open_page_and_wait(self, url):
        #self.driver.get(url)
        #WebDriverWait(self.driver, 5).until()
