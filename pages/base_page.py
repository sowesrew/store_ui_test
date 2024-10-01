from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePageStore:
    def __init__(self, driver):
        self.driver = driver

    def wait_element_to_clickable(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(element))
        return self.driver.find_element(*element)

    def open_page(self, url):
        self.driver.get(url)

    def click_element(self, element):
        element.click()

    #def open_page_and_wait(self, url):
        #self.driver.get(url)
        #WebDriverWait(self.driver, 5).until()
