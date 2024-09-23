import allure
from data import DataUrl
from pages.main_page import MainPageStore
from conftest import driver


class TestNavigationMainPage:

    @allure.title("Переход на главную страницу из вкладки Cart")
    def test_go_to_home(self, driver):
        home = MainPageStore(driver)
        home.open_page(DataUrl.BASE_URL + DataUrl.CART)
        home.click_logo()
        assert driver.current_url == DataUrl.BASE_URL + DataUrl.HOME

    @allure.title("Переход из карточки товара на главную страницу")
    def test_go_to_home_cart(self, driver):
        home = MainPageStore(driver)
        home.open_page(DataUrl.BASE_URL + DataUrl.PRODUCT_NOT_ID + '1')
        home.click_logo()
        assert driver.current_url == DataUrl.BASE_URL + DataUrl.HOME

