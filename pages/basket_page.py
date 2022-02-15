from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    # проверяем, что в корзине нет товара
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEM),\
            "Basket is not empty but should be"

    # проверяем, что есть сообщение о том, что корзина пуста
    def should_be_message_about_basket_is_empty(self):
        basket_is_empty = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).get_attribute("href")
        basket_url = self.browser.current_url
        assert basket_is_empty in basket_url, "Basket is not empty"
