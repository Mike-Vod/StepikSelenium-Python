from selenium import webdriver
from selenium.webdriver.support.ui import Select


link="http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome("C:\Python\chromedriver.exe")
browser.get(link)

x = browser.find_element_by_css_selector('[id = "num1"]').text
y = browser.find_element_by_css_selector('[id = "num2"]').text
result = str(int(x) + int(y))

select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(result)


button = browser.find_element_by_css_selector("button.btn")
button.click()
