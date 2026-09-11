import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)

button = browser.find_element(By.TAG_NAME, "button")
button.click()

confirm = browser.switch_to.alert
time.sleep(2)
confirm.dismiss()
time.sleep(2)

button.click()
confirm.accept()

x_web = browser.find_element(By.ID, "input_value")
x = int(x_web.text)

expr_str = "ln(abs(12*sin(x)))"
expr_py = expr_str.replace("ln", "math.log").replace("sin", "math.sin")
answer = str(eval(expr_py))

answ_input = browser.find_element(By.TAG_NAME, "input")
answ_input.send_keys(answer)

button2 = browser.find_element(By.TAG_NAME, "button")
button2.click()
time.sleep(10)
browser.quit()
