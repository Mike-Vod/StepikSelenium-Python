from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome("C:\Python\chromedriver.exe")

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), ('10000'))
    )
button = browser.find_element_by_css_selector('.btn')
button.click()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('span#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer.form-control')
input.send_keys(y)

button = browser.find_element_by_css_selector("#solve")
button.click()