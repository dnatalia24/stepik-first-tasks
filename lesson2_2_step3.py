# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x = browser.find_element_by_id('num1')
    y = browser.find_element_by_id('num2')

    x_result = x.text
    y_result = y.text

    result = str(int(x_result) + int(y_result))

    from selenium.webdriver.support.ui import Select

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(result)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()