from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_message_that_product_add_to_basket()
    page.should_be_product_name_in_message()
    page.should_be_message_with_product_price()
    page.should_be_product_price_in_message()
