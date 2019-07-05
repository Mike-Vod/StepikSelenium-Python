from selenium import webdriver
import os


link="http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome("C:\Python\chromedriver.exe")
browser.get(link)

input1 = browser.find_element_by_css_selector('[name=firstname]')
input1.send_keys('Серж')
input2 = browser.find_element_by_css_selector('[name=lastname]')
input2.send_keys('Серж')
input3 = browser.find_element_by_css_selector('[name=email]')
input3.send_keys('mail@nail.ru')

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
element = browser.find_element_by_css_selector('[name=file]')
element.send_keys(file_path)
button = browser.find_element_by_css_selector("button.btn")
button.click()
