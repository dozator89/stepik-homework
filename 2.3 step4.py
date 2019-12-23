from selenium import webdriver
import time
import os
import math

def calc(x):
    #return str(math.log(abs(12*math.sin(x))))
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    submit_locator = browser.find_element_by_class_name('btn.btn-primary')
    submit_locator.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_locator = browser.find_element_by_id("input_value")
    x = x_locator.text
    y = calc(int(x))

    txt_locator = browser.find_element_by_id("answer")
    txt_locator.send_keys(str(y))

    submit_locator = browser.find_element_by_class_name('btn.btn-primary')
    submit_locator.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()