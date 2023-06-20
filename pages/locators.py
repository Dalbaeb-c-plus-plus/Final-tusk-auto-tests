from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") 
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    ADD_TO_BUSKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    MSG_ABOUT_ADDED_PRODUCT = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")
    BUSKET_PRICE = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    REAL_PRICE = (By.CSS_SELECTOR, "#content_inner > article > table > tbody > tr:nth-child(3) > td")
    MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")