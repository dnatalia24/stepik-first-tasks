# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    inside_treasure = browser.find_element_by_id('treasure')
    x_element = inside_treasure.get_attribute('valuex')
    x = x_element
    y = calc(x)

    print(x)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)

    input2 = browser.find_element_by_id("robotCheckbox")
    input2.click()

    input2 = browser.find_element_by_id("robotsRule")
    input2.click()

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()