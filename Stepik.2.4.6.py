from selenium import webdriver


browser = webdriver.Chrome("C:\Python\chromedriver.exe")
browser.get("http://suninjuly.github.io/cats.html")

button = browser.find_element_by_id("button")
button.click()
message = browser.find_element_by_id("check_message")

assert "успешно" in message.text