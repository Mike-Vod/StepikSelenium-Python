from selenium import webdriver
import time
import math

link="http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome("C:\Python\chromedriver.exe")
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

capture_find = browser.find_element_by_css_selector('img')
capture_valuex = capture_find.get_attribute('valuex')
x = capture_valuex
y = calc(x)

#x_element = browser.find_element_by_css_selector('span#input_value')
#x = x_element.text
#y = calc(x)

input = browser.find_element_by_css_selector('#answer')
input.send_keys(y)

option1 = browser.find_element_by_css_selector('#robotCheckbox')
option1.click()
option2 = browser.find_element_by_css_selector('#robotsRule')
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()