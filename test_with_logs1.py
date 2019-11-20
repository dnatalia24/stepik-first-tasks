# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
import time

class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
    # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input:required.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input:required.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input:required.third")
        input3.send_keys("fortestonly@gmail.com")

    # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
        time.sleep(1)


        self.assertEqual(browser.find_element_by_tag_name("h1").text, "Поздравляем! Вы успешно зарегистировались!", 'Error Registration 1')

if __name__ == "__main__":
    unittest.main()