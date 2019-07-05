from selenium import webdriver
import time
import math

link="https://suninjuly.github.io/math.html"
browser = webdriver.Chrome("C:\Python\chromedriver.exe")
browser.get(link)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_css_selector('span#input_value')
x = x_element.text
y = calc(x)

input = browser.find_element_by_css_selector('#answer.form-control')
input.send_keys(y)

option1 = browser.find_element_by_css_selector('#robotCheckbox')
option1.click()
option2 = browser.find_element_by_css_selector('#robotsRule')
option2.click()
button = browser.find_element_by_css_selector("button.btn")
button.click()

#input1.send_keys("Петечка")
#input2 = browser.find_element_by_css_selector(".first_block > .second_class > .second")
#input2.send_keys("Укбоев")
#input3 = browser.find_element_by_css_selector(".first_block > .third_class > .third")
#input3.send_keys("a.dctest@yandex.ru")
#button = browser.find_element_by_css_selector("button.btn")
#button.click()
#Проверяем, что смогли зарегистрироваться
#ждем загрузки страницы
#time.sleep(1)

# находим элемент, содержащий текст
#welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
#welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
#assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text