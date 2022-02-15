from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage


class TestLoginFromMainPage:
    # тест для проверки перехода на страницу авторизации/регистрации с главной страницы
    def test_guest_can_go_to_login_page_from_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com"
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    # тест для проверки отображения на главной странице ссылки для перехода на страницу авторизации/регистрации
    def test_guest_should_see_login_link_on_main_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

# тест для проверки отсутствия товара в корзине при переходе с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_message_about_basket_is_empty()
