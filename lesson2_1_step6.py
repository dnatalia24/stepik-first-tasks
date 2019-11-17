# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

    button_state = browser.find_element_by_css_selector("button.btn")
    button_disabled = button_state.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

    time.sleep(10)
    button_disabled = button_state.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()