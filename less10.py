import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()
browser.get(link)

firstName = browser.find_element(By.NAME, "firstname")
firstName.send_keys("OO")

lastName = browser.find_element(By.NAME, "lastname")
lastName.send_keys("P")

email = browser.find_element(By.NAME, "email")
email.send_keys("S")

file = browser.find_element(By.CSS_SELECTOR, "[accept='.txt']")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'less10.txt')
file.send_keys(file_path)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

time.sleep(10)
browser.quit()













# current_dir = os.path.abspath(os.path.dirname(__file__))
# file_path = os.path.join(current_dir, 'file.text')
# # element.send_keys(file_path)
#
# print(os.path.abspath(__file__))
# print(os.path.abspath(os.path.dirname(__file__)))