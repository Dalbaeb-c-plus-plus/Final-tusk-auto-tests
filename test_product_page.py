import pytest
from selenium.webdriver.common.by import By
from pages.product_page import ProductPage
import time
  
@pytest.mark.parametrize('links_number', ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
def test_guest_can_add_product_to_busket(browser, links_number):
   try:
       link =f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{links_number}"
       print(link)
       page = ProductPage (browser, link, links_number)
       page.open()
       page.add_product_to_busket()
       page.solve_quiz_and_get_code()
       page.should_be_msg()
       page.compare_added_and_real()
       page.compare_price()
   finally:
       browser.quit ()