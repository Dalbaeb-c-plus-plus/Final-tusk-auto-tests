from pages.main_page import MainPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By
import time

def test_guest_can_go_to_login_page(browser):
  try:
    link = "http://selenium1py.pythonanywhere.com/"
    page1 = MainPage(browser, link)
    page2 = LoginPage(browser, link) 
    page1.open()
    page1.go_to_login_page()
    page1.should_be_login_link()
    page2.should_be_login_url()
    page2.should_be_login_form()
    page2.should_be_register_form()
  finally:
    browser.quit ()