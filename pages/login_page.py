from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print("Проверка соответсвия ссылки")
        assert "login" in self.browser.current_url, "Not */login* in url"

    def should_be_login_form(self):
        print("Проверка наличия области логина")
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN FORM  is not presented"
        
    def should_be_register_form(self):
        print("Проверка наличия области регистрации")
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER FORM  is not presented"
