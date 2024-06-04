from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

try:
    chrome.get("http://the-internet.herokuapp.com/inputs")
    input_field = chrome.find_element(
        By.TAG_NAME, "input")
    input_field.send_keys("1000")
    input_field.clear()
    input_field.send_keys("999")

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
