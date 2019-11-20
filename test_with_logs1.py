# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
import time
#version1.0
class TestReg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
    # fill in the mandatory fields
        input1 = browser.find_element_by_css_selector("input:required.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("input:required.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("input:required.third")
        input3.send_keys("fortestonly@gmail.com")

    # sent the filled in form
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

    # waiting for page loading
        time.sleep(1)


        self.assertEqual(browser.find_element_by_tag_name("h1").text, "Congratulations! You have successfully registered!", 'Error Registration 1')
        time.sleep(10)
if __name__ == "__main__":
    unittest.main()