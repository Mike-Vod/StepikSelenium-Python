from selenium import webdriver
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link="http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome("C:\Python\chromedriver.exe")
browser.get(link)

element = browser.find_element_by_css_selector('.trollface')
element.click()

new_window = browser.window_handles[1]
browser.switch_to.window(new_window)



x_element = browser.find_element_by_css_selector('span#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer.form-control')
input.send_keys(y)

button = browser.find_element_by_css_selector(".btn")
button.click()

