from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    #return str(math.log(abs(12*math.sin(x))))
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_locator = browser.find_element_by_id("input_value")
    x = x_locator.text
    # second_locator = browser.find_element_by_id("num2")
    y = calc(int(x))

    txt_locator = browser.find_element_by_id("answer")
    txt_locator.send_keys(str(y))
    browser.execute_script("return arguments[0].scrollIntoView(true);", txt_locator)

    notrobot_locator = browser.find_element_by_id("robotCheckbox")
    notrobot_locator.click()
    #
    robots_rules = browser.find_element_by_id("robotsRule")
    robots_rules.click()

    button = browser.find_element_by_tag_name("button")
    button.click()




    # select = Select(browser.find_element_by_tag_name("select"))
    # select.select_by_value(str(y))
    #
    # submit_btn = browser.find_element_by_xpath("//button[@type='submit']")
    # submit_btn.click()




finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()