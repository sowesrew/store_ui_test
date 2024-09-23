from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = [By.XPATH, "//*[@id='nava']"]  # логотип ?

    # меню
    HOME = [By.XPATH, "//*[@id='navbarExample']/ul/li[1]"]  # Home
    CONTACT = [By.XPATH, "//*[@id='navbarExample']/ul/li[2]"]  # Соntact
    ABOUT_US = [By.XPATH, "//*[@id='navbarExample']/ul/li[3]"]  # About Us
    CART = [By.XPATH, "//*[@id='navbarExample']/ul/li[4]"]  # Cart
    LOG_IN = [By.XPATH, "//*[@id='navbarExample']/ul/li[5]"]  # Log in
    SIGN_UP_LOGOUT = [By.XPATH, "//*[@id='navbarExample']/ul/li[6]"]  # Sign up/ Log Out

    LEFT_SLIDER = [By.XPATH, "//*[@id='carouselExampleIndicators']/a[1]"]  # левый слайдер на главной странице
    RIGHT_SLIDER = [By.XPATH, "//*[@id='carouselExampleIndicators']/a[2]"]  # правый слайдер на главной странице

    CATEGORIES = [By.XPATH, "//*[@id='cat']"]  # заголовок Categories
    PHONES = [By.XPATH, "//*[@onclick='byCat('phone')']"]  # заголовок Phones
    LAPTOPS = [By.XPATH, "//*[@onclick='byCat('notebook')']"]  # заголовок Laptops
    MONITORS = [By.XPATH, "//*[@onclick='byCat('monitor')']"]  # заголовок Monitors

    IMG = [By.XPATH, "//*[@id='tbodyid']/div[1]/div/a/img"]  # картинка 1 элемента
    LINK = [By.XPATH, "//*[@id='tbodyid']/div[2]/div/div/h4"]  # ссылка 2 элемента

    PREVIOUS = [By.XPATH, "//*[@id='prev2']"]  # кнопка "Назад"
    NEXT = [By.XPATH, "//*[@id='next2']"]  # кнопка "Вперёд"
