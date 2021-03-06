import pytest
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time

values = [
            "offer0",
            "offer1",
            "offer2",
            "offer3",
            "offer4",
            "offer5",
            "offer6",
            pytest.param("offer7", marks=pytest.mark.xfail(reason="bug")),
            "offer8",
            "offer9",
        ]


class TestLoginFromProductPage:
    # тест для проверки перехода на страницу авторизации/регистрации со страницы товара
    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # тест для проверки отображения на странице товара ссылки для перехода на страницу авторизации/регистрации
    def test_guest_should_see_login_link_on_product_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


# тесты для проверки того, что отображается/не отображается сообщение об успешном добавлении товара в корзину
class TestSuccessMessage:
    @pytest.mark.xfail(reason="negative test")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message_with_is_not_element_present()

    def test_guest_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message_with_is_not_element_present()

    @pytest.mark.xfail(reason="negative test")
    def test_message_disappeared_after_adding_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_not_be_success_message_with_is_disappeared()


class TestUserAddToBasketFromProductPage:
    # регистрируем пользователя и проверяем, что регистрация прошла успешно
    # метод выполняется перед прохождением каждого теста внутри класса
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "KanIOq0de3"
        link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    # тест для проверки добавления товара в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_message_that_product_add_to_basket()
        page.should_be_product_name_in_message()
        page.should_be_message_with_product_price()
        page.should_be_product_price_in_message()

    # тест для проверки того, что не отображается сообщение об успешном добавлении товара в корзину
    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message_with_is_not_element_present()

# тест для проверки добавления товара в корзину
@pytest.mark.need_review
@pytest.mark.parametrize("promo_value", values)
def test_guest_can_add_product_to_basket(browser, promo_value):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={promo_value}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_message_that_product_add_to_basket()
    page.should_be_product_name_in_message()
    page.should_be_message_with_product_price()
    page.should_be_product_price_in_message()


# тест для проверки отсутствия товара в корзине при переходе со страницы товара
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_about_basket_is_empty()
