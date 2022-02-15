from selenium.webdriver.common.by import By


# локаторы для страницы корзины
class BasketPageLocators:
    BASKET_ITEM = (By.CSS_SELECTOR, ".basket_items")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner [href]")


# базовые локаторы
class BasePageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".alert")


# локаторы для страницы авторизации/регистрации
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")


# локаторы для главной страницы
class MainPageLocators:
    pass

# локаторы для страницы с товаром
class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    MESSAGE_THAT_PRODUCT_ADD_TO_BASKET = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) strong")
    MESSAGE_WITH_PRODUCT_PRICE = (By.CSS_SELECTOR, "#messages .alert:nth-child(3) strong")
