from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    firefox.get("http://the-internet.herokuapp.com/inputs")
    input_field = firefox.find_element(
        By.TAG_NAME, "input")
    input_field.send_keys("1000")
    input_field.clear()
    input_field.send_keys("999")

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
