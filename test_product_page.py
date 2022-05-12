import pytest
from .pages.main_page import MainPage
from .pages.basket_page import BasketPage
from .pages.product_page import Page_Object
from .pages.login_page import LoginPage
from selenium.common.exceptions import NoAlertPresentException


@pytest.mark.user
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)     
    def setup(self, browser):
        link="http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)   
        page.open()
        page.should_be_login_url()
        page.register_new_user()
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"
        page = Page_Object(browser, link)   
        page.open()
        page.should_not_be_success_message()
        
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = Page_Object(browser, link)   
        page.open()                     
        page.should_be_added_to_basket()
        page.should_be_message()
        page.should_be_correct_basket()

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = Page_Object(browser, link)   
    page.open()                     
    page.should_be_added_to_basket()
    page.should_be_message()
    page.should_be_correct_basket()    

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = Page_Object(browser, link)   
    page.open()
    page.should_be_added_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link ="http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = Page_Object(browser, link)   
    page.open()
    page.should_be_added_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_disappeared_element()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Page_Object(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Page_Object(browser, link)
    page.open()
    page.should_be_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = Page_Object(browser, link)
    page.open()
    page.should_go_to_basket_from_site_header()
    page = BasketPage(browser, link)
    page.open()
    page.should_not_be_items_in_basket()
    page.should_be_message_about_empty_basket()