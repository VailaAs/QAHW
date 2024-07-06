from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    firefox.get("http://the-internet.herokuapp.com/login")

    username_field = firefox.find_element(
        By.ID, "username")
    username_field.send_keys('tomsmith')

    password_field = firefox.find_element(
        By.ID, "password")
    password_field.send_keys('SuperSecretPassword!')

    login_button = firefox.find_element(
        By.CSS_SELECTOR, "#login > button > i")
    login_button.click()

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
