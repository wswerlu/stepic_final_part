from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    # добавляем товар в корзину
    def add_product_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()
        self.solve_quiz_and_get_code()

    # проверяем, что есть сообщение о том, что товар добавлен в корзину
    def should_be_message_that_product_add_to_basket(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_THAT_PRODUCT_ADD_TO_BASKET), \
            "No message that product add to basket"

    # проверяем, что в сообщении о том, что товар добавлен в корзину, есть название добавленного товара
    def should_be_product_name_in_message(self):
        message_that_product_add_to_basket = \
            self.browser.find_element(*ProductPageLocators.MESSAGE_THAT_PRODUCT_ADD_TO_BASKET).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert product_name == message_that_product_add_to_basket, \
            "Product name is not in message that product add to basket"

    # проверяем, что есть сообщение с ценой товара
    def should_be_message_with_product_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRODUCT_PRICE), \
            "No message with product price"

    # проверяем, что в сообщении с ценой товара указана цена
    def should_be_product_price_in_message(self):
        message_with_product_price = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRODUCT_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == message_with_product_price, \
            "Product price is not in message that product add to basket"

    # проверяем, что не появилось сообщение об успешном добавлении товара в корзину
    # реализация с помощью метода is_not_element_present
    def should_not_be_success_message_with_is_not_element_present(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_THAT_PRODUCT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    # проверяем, что не появилось сообщение об успешном добавлении товара в корзину
    # реализация с помощью метода is_disappeared
    def should_not_be_success_message_with_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_THAT_PRODUCT_ADD_TO_BASKET), \
            "Success message is presented, but should not be"
