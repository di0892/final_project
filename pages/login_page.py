from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import BasePageLocators
import time

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert self.browser.find_element(*BasePageLocators.LOGIN_LINK)

    def should_be_login_form(self):
        assert self.browser.find_element(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.browser.find_element(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self):
        email_textarea = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_textarea.send_keys(str(time.time()) + "@fakemail.org")
        password1_textarea = self.browser.find_element(*LoginPageLocators.PASSWORD1)
        password1_textarea.send_keys("Z2unLmIBF")
        password2_textarea = self.browser.find_element(*LoginPageLocators.PASSWORD2)
        password2_textarea.send_keys("Z2unLmIBF")
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button.click()