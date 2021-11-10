from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time
from selenium.webdriver.support.select import Select
import os

def calc(x):
  res = math.log(abs(12 * math.sin(x)))
  return str(res)

browser = webdriver.Chrome()
browser.implicitly_wait(5)
browser.get("http://suninjuly.github.io/explicit_wait2.html")
y = browser.find_element_by_css_selector("#book")
a = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
y.click()

# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)

x = browser.find_element_by_css_selector("#input_value").text
x = int(x)

res = calc(x)

enter = browser.find_element_by_css_selector("#answer")
enter.send_keys(res)

submit = browser.find_element_by_css_selector("body > form > div > div > button")
webdriver.ActionChains(browser).move_to_element(submit).perform()
submit.click()

time.sleep(15)
browser.quit()