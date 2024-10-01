import allure
from data import DataUrl
from pages.main_page import MainPageStore
from conftest import driver
from locators.main_page_locators import MainPageLocators
from locators.cart_page_locators import CartPageLocators
from selenium.webdriver.support import expected_conditions
import conftest
import time


class TestMainPage:

    #@allure.title("Переключение слайдера вправо")
    #def test_switch_right_slide(self, driver):
        #home = MainPageStore(driver)
        #home.open_page(DataUrl.BASE_URL)
        #home.wait_element_to_clickable(MainPageLocators.RIGHT_SLIDER)
        #home.click_right_slider()
        #active_slider = MainPageLocators.ACTIVE_SL
        #assert active_slider in MainPageLocators.SLIDER_2

    @allure.title("Переключение на вкладку Laptops")
    def test_switch_lap(self, driver):
        home = MainPageStore(driver)
        home.open_page(DataUrl.BASE_URL)
        home.click_laptops()
        home.wait_element_to_clickable(MainPageLocators.TEXT_LAP)
        sony_card = home.first_cart_lap()
        home.wait_element_to_clickable(MainPageLocators.TEXT_LAP)
        assert sony_card.text == 'Sony vaio i5'

    @allure.title("Переключение на вкладку Monitors")
    def test_switch_mon(self, driver):
        home = MainPageStore(driver)
        home.open_page(DataUrl.BASE_URL)
        home.click_monitors()
        home.wait_element_to_clickable(MainPageLocators.TEXT_MON)
        sony_card = home.first_cart_mon()
        home.wait_element_to_clickable(MainPageLocators.TEXT_MON)
        assert sony_card.text == 'Apple monitor 24'

    @allure.title("Переключение на вкладку Phones")
    def test_switch_ph(self, driver):
        home = MainPageStore(driver)
        home.open_page(DataUrl.BASE_URL)
        home.click_monitors()
        home.wait_element_to_clickable(MainPageLocators.TEXT_MON)
        home.click_phones()
        home.wait_element_to_clickable(MainPageLocators.TEXT_PH)
        sony_card = home.first_cart_ph()
        home.wait_element_to_clickable(MainPageLocators.TEXT_PH)
        assert sony_card.text == 'Samsung galaxy s6'

    @allure.title("Переход в карточку")
    def test_go_to_cart(self, driver):
        home = MainPageStore(driver)
        home.open_page(DataUrl.BASE_URL)
        home.wait_element_to_clickable(MainPageLocators.FIRST_CART)
        home.click_cart()
        home.wait_element_to_clickable(CartPageLocators.ADD_TO_CART)
        assert driver.current_url == DataUrl.BASE_URL + DataUrl.PRODUCT_NOT_ID + '1'
