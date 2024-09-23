from pages.base_page import BasePageStore
from locators.main_page_locators import MainPageLocators


class MainPageStore(BasePageStore):
    def click_logo(self):
        element = self.driver.find_element(*MainPageLocators.LOGO)
        self.click_element(element)

