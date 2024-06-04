from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

try:
    chrome.get("http://the-internet.herokuapp.com/login")

    username_field = chrome.find_element(
        By.ID, "username")
    username_field.send_keys('tomsmith')

    password_field = chrome.find_element(
        By.ID, "password")
    password_field.send_keys('SuperSecretPassword!')

    login_button = chrome.find_element(
        By.CSS_SELECTOR, "#login > button > i")
    login_button.click()

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
