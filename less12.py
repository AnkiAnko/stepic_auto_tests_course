import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
button.click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)

x_web = browser.find_element(By.ID, "input_value")
x = int(x_web.text)

expr_str = "ln(abs(12*sin(x)))"
expr_py = expr_str.replace("ln", "math.log").replace("sin", "math.sin")
answer = str(eval(expr_py))

input_field = browser.find_element(By.ID, "answer")
input_field.send_keys(answer)

button2 = browser.find_element(By.TAG_NAME, "button")
button2.click()

alert = browser.switch_to.alert
time.sleep(10)
alert.accept()

time.sleep(1)
browser.quit()