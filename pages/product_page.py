from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException  

class ProductPage(BasePage):
    def add_product_to_busket(self):
        print("Добавление товара в корзину")
        butn_busket = self.browser.find_element(*ProductPageLocators.ADD_TO_BUSKET)
        butn_busket.click()
    
    def should_be_msg(self):
        print("Проверка наличия сообщения о добавлении в корзину")
        assert self.is_element_present(*ProductPageLocators.MSG), "Massege  is not presented"

    def compare_added_and_real(self):
        print("Сравнение названия добавленого и реального товаров")
        product_real =str (self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text)
        product_added = str (self.browser.find_element(*ProductPageLocators.MSG_ABOUT_ADDED_PRODUCT).text)
        assert product_real == product_added, "Названия продуктов добавленого и реального различны"

    def compare_price(self):
        print("Сравнение цен добавленого и реального товаров")
        price_real = self.browser.find_element(*ProductPageLocators.REAL_PRICE).text
        price_busket = self.browser.find_element(*ProductPageLocators.BUSKET_PRICE).text
        assert price_real == price_busket, "Цены продуктов добавленого и реального различны"