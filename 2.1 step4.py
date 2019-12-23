import math
from selenium import webdriver
import time


def calc(x):
    #return str(math.log(abs(12*math.sin(x))))
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # x_element = browser.find_element_by_id("input_value")
    # x = x_element.text
    # y = calc(x)
    #
    # input_element = browser.find_element_by_id("answer")
    # input_element.send_keys(y)
    #
    # notrobot_element = browser.find_element_by_id("robotCheckbox")
    # notrobot_element.click()

    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value if people radio: ", people_checked)
    #assert people_checked is not None, "People radio is not selected by default"
    assert people_checked == "true", "People radio is not selected by default"

    robotrule_element = browser.find_element_by_id("robotsRule")
    #robotrule_element.click()
    robots_checked = robotrule_element.get_attribute("checked")
    assert robots_checked is None

    # submit_element = browser.find_element_by_xpath("//button[@class='btn btn-default']")
    # submit_element.click()



finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(1)
    # закрываем браузер после всех манипуляций
    browser.quit()