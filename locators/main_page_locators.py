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

    IMG_1 = [By.XPATH, "//*[@id='carouselExampleIndicators']/div/div/img[@alt= 'First slide']/.."]  # Первый элемент карусели
    IMG_2 = [By.XPATH, "//*[@id='carouselExampleIndicators']/div/div/img[@alt= 'Second slide']/.."]  # Второй элемент карусели
    IMG_3 = [By.XPATH, "//*[@id='carouselExampleIndicators']/div/div/img[@alt= 'Third slide']/.."]  # Третий элемент карусели
    ACTIVE = [By.XPATH, "//*[@id='carouselExampleIndicators']/div/div[contains(@class,'active')]"]  # Активный слайдер
    ACTIVE_IMG_1 = [By.XPATH, ".//div[@class='carousel-item active']/img[@alt= 'First slide]"]
    ACTIVE_IMG_2 = [By.XPATH, ".//div[@class='carousel-item active']/img[@alt= 'Second slide]"]
    ACTIVE_IMG_3 = [By.XPATH, ".//div[@class='carousel-item active']/img[@alt= 'Third slide']"]
    SLIDER_2 = [By.XPATH, "//*[@id='carouselExampleIndicators']/ol/li[2]"]
    ACTIVE_SL = [By.CLASS_NAME, "active"]


    CATEGORIES = [By.XPATH, "//*[@id='cat']"]  # заголовок Categories
    PHONES = [By.XPATH, "//a[text() = 'Phones']"]  # заголовок Phones
    LAPTOPS = [By.XPATH, "//a[text() = 'Laptops']"]  # заголовок Laptops
    MONITORS = [By.XPATH, "//a[text() = 'Monitors']"]  # заголовок Monitors

    TEXT_LAP = [By.XPATH, "//a[text() = 'Sony vaio i5']"]  # текст 1 элемента на странице Laptop
    TEXT_MON = [By.XPATH, "//a[text() = 'Apple monitor 24']"]  # текст 1 элемента на страницe Monitors
    TEXT_PH = [By.XPATH, "//a[text() = 'Samsung galaxy s6']"]  # текст 1 элемента на странице Phones

    FIRST_CART = [By.XPATH, "//*[@id='tbodyid']/div[1]/div[@class = 'card h-100']"]  # первая карточка

    PREVIOUS = [By.XPATH, "//*[@id='prev2']"]  # кнопка "Назад"
    NEXT = [By.XPATH, "//*[@id='next2']"]  # кнопка "Вперёд"
