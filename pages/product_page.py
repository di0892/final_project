from .base_page import BasePage
from .locators import ObjectPageLocators

class Page_Object(BasePage):
    def should_be_added_to_basket(self):
        add_to_basket=self.browser.find_element(*ObjectPageLocators.BASKET_BUTTON)
        add_to_basket.click()
        

    def should_be_message(self):
        name_in_product = self.browser.find_element(*ObjectPageLocators.PRODUCT_NAME)
        name_in_product = name_in_product.text
        name_in_message = self.browser.find_element(*ObjectPageLocators.MESSAGE_NAME)
        name_in_message = name_in_message.text
        assert name_in_product == name_in_message, "Wrong title"
        
    def should_be_correct_basket(self):
        price_in_product = self.browser.find_element(*ObjectPageLocators.PRODUCT_PRICE)
        price_in_product = price_in_product.text
        price_in_basket = self.browser.find_element(*ObjectPageLocators.BASKET_PRICE)
        price_in_basket = price_in_basket.text
        assert price_in_product == price_in_basket, "Wrong sum"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ObjectPageLocators.MESSAGE_NAME), \
           "Success message is presented, but should not be"

    def should_be_disappeared_element(self):
        assert self.is_disappeared(*ObjectPageLocators.MESSAGE_NAME), \
           "Element is not disappeared, but it should"