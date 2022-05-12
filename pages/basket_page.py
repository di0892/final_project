from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.NO_ITEMS_IN_BASKET),\
               "items in basket, but should not be"
         
    def should_be_message_about_empty_basket(self):
        assert self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE),\
               "no text that the basket is empty"