import math
from selenium import webdriver
import time

def calc(x):
    #return str(math.log(abs(12*math.sin(x))))
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    img = browser.find_element_by_id("treasure")
    valuex = img.get_attribute("valuex")
    y = calc(valuex)

    input_element = browser.find_element_by_id("answer")
    input_element.send_keys(y)

    notrobot_element = browser.find_element_by_id("robotCheckbox")
    notrobot_element.click()

    robotrule_element = browser.find_element_by_id("robotsRule")
    robotrule_element.click()

    submit_element = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    submit_element.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()