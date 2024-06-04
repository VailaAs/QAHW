from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
 browser.get("http://the-internet.herokuapp.com/entry_ad")
 sleep(5)
 browser.find_element(By.CSS_SELECTOR, '.modal-footer').click()

except Exception as ex:
 print(ex)
finally:
 browser.quit()