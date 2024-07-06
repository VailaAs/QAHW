from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

chrome = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

try:
    chrome.get("http://the-internet.herokuapp.com/entry_ad")
    sleep(5)
    chrome.find_element(
        By.CSS_SELECTOR, '.modal-footer').click()

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
