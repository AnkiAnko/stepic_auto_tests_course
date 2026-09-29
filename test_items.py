import time
import pytest
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_basket_button(browser):
    browser.get(link)
    time.sleep(30)
    basket_button = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    assert basket_button is not None, "Buttoon 'Add to basket' not found!"

