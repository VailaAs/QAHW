from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

firefox = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    firefox.get("http://the-internet.herokuapp.com/entry_ad")
    sleep(5)
    firefox.find_element(
        By.CSS_SELECTOR, '.modal-footer').click()

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
