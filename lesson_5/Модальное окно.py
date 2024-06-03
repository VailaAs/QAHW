from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
 chrome.get("http://the-internet.herokuapp.com/entry_ad")
 firefox.get("http://the-internet.herokuapp.com/entry_ad")
 sleep(5)
 chrome.find_element(By.CSS_SELECTOR, '.modal-footer').click()
 firefox.find_element(By.CSS_SELECTOR, '.modal-footer').click()

except Exception as ex:
 print(ex)
finally:
 chrome.quit()
 firefox.quit()