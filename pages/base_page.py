from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from .locators import MainPageLocators
import math

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def open(self): 
        print("Открытие сайта")
        self.browser.get(self.url)  
    def should_be_login_link(self):
        print("Проверка наличия ссылки на авторизaцию")
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    def is_element_present(self, how, what):
        try:
           self.browser.find_element(how, what)
        except (NoSuchElementException):
           return False
        return True

    def solve_quiz_and_get_code(self):
        print("Расчет кода")
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
           alert = self.browser.switch_to.alert
           alert_text = alert.text
           print(f"Your code: {alert_text}")
           alert.accept()
        except NoAlertPresentException:
           print("No second alert presented")