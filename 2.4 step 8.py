from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button = browser.find_element_by_id("book")
    button.click()

    x_locator = WebDriverWait(browser, 1).until(
            EC.presence_of_element_located((By.XPATH, "//span[@id='input_value']"))
        )
    x = x_locator.text
    print(x)
    y = calc(int(x))

    txt_locator = browser.find_element_by_id("answer")
    txt_locator.send_keys(str(y))

    submit_locator = WebDriverWait(browser, 1).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary'))
    )
    submit_locator.click()

finally:
    # ожиданиеa чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

