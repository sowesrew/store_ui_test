from selenium.webdriver.common.by import By


class CartPageLocators:
    ADD_TO_CART = [By.XPATH, "//*[@id='tbodyid']/div[2]/div/a[text() = 'Add to cart']"]  # кнопка Add to cart
