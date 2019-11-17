# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()

    alert = browser.switch_to_alert()
    alert.accept()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input = browser.find_element_by_id('answer')
    input.send_keys(y)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()