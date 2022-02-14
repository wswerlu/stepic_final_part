from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

    def should_be_message_that_product_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_THAT_PRODUCT_ADD_TO_BASKET), \
            "No message that product add to basket"

    def should_be_product_name_in_message(self):
        message_that_product_add_to_basket = \
            self.browser.find_element(*ProductPageLocators.MESSAGE_THAT_PRODUCT_ADD_TO_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == message_that_product_add_to_basket, \
            "Product name is not in message that product add to basket"

    def should_be_message_with_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRODUCT_PRICE), \
            "No message with product price"

    def should_be_product_price_in_message(self):
        message_with_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRODUCT_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_with_product_price, \
            "Product price is not in message that product add to basket"

    def should_not_be_success_message_with_is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_THAT_PRODUCT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def should_not_be_success_message_with_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_THAT_PRODUCT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"
