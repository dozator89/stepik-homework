from selenium import webdriver
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_locator = browser.find_element_by_name("firstname")
    second_locator = browser.find_element_by_name("lastname")
    email_locator = browser.find_element_by_name("email")

    first_locator.send_keys("EraName")
    second_locator.send_keys("EraSecond")
    email_locator.send_keys("EraMail")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'temp.txt')

    file_locator = browser.find_element_by_xpath("//input[@type='file']")
    file_locator.send_keys(file_path)

    submit_locator = browser.find_element_by_class_name('btn.btn-primary')
    submit_locator.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()