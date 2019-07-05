from selenium import webdriver
import math

link="https://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome("C:\Python\chromedriver.exe")
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('span#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer')
input.send_keys(y)
browser.execute_script("window.scrollBy(0, 100);")
option1 = browser.find_element_by_css_selector('#robotCheckbox')
option1.click()
option2 = browser.find_element_by_css_selector('#robotsRule')
option2.click()
browser.execute_script("window.scrollBy(0, 100);")
button = browser.find_element_by_css_selector("button.btn")
button.click()
