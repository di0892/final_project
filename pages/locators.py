from selenium.webdriver.common.by import By

class MainPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, "span a.btn.btn-default[href]")
       
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[value=Register]")

class ObjectPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "button[value]")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div h1")
    MESSAGE_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    NO_ITEMS_IN_BASKET = (By.CSS_SELECTOR, "#basket_formset")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div p")