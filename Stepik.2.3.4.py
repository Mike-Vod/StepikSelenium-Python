from selenium import webdriver
import math

link="http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome("C:\Python\chromedriver.exe")
browser.get(link)

button = browser.find_element_by_css_selector(".btn")
button.click()

confirm = browser.switch_to.alert
confirm.accept()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('span#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer.form-control')
input.send_keys(y)

button = browser.find_element_by_css_selector(".btn")
button.click()