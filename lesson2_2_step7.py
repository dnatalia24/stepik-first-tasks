# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math
import os

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Nata')

    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Drozdovska')

    input3 = browser.find_element_by_name('email')
    input3.send_keys('drozdik@gmail.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
    element = browser.find_element_by_id('file').send_keys('/Users/ndrozdovska/selenium_course/file.txt')

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()