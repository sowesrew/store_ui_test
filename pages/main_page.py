from pages.base_page import BasePageStore
from locators.main_page_locators import MainPageLocators


class MainPageStore(BasePageStore):

    def click_logo(self):
        element = self.driver.find_element(*MainPageLocators.LOGO)
        self.click_element(element)

    def click_right_slider(self):
        element = self.driver.find_element(*MainPageLocators.RIGHT_SLIDER)
        self.click_element(element)

    def click_laptops(self):
        element = self.driver.find_element(*MainPageLocators.LAPTOPS)
        self.click_element(element)

    def first_cart_lap(self):
        element = self.driver.find_element(*MainPageLocators.TEXT_LAP)
        return element

    def click_monitors(self):
        element = self.driver.find_element(*MainPageLocators.MONITORS)
        self.click_element(element)

    def first_cart_mon(self):
        element = self.driver.find_element(*MainPageLocators.TEXT_MON)
        return element

    def click_phones(self):
        element = self.driver.find_element(*MainPageLocators.PHONES)
        self.click_element(element)

    def first_cart_ph(self):
        element = self.driver.find_element(*MainPageLocators.TEXT_PH)
        return element

    def click_cart(self):
        element = self.driver.find_element(*MainPageLocators.FIRST_CART)
        self.click_element(element)