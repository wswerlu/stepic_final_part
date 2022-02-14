import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


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


@pytest.mark.xfail(reason="wrong test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message_with_is_not_element_present()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_with_is_not_element_present()


@pytest.mark.xfail(reason="wrong test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message_with_is_disappeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
