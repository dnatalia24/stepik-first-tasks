# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    link = "http://suninjuly.github.io/wait1.html"
    browser.get(link)

    button = browser.find_element_by_id("verify")
    button.click()
    message = browser.find_element_by_id("verify_message")

    assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()