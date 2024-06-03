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
 chrome.get("http://the-internet.herokuapp.com/inputs")
 firefox.get("http://the-internet.herokuapp.com/inputs")
 inputC = chrome.find_element(By.TAG_NAME, "input")
 inputC.send_keys(1000)
 InputF = firefox.find_element(By.TAG_NAME, "input")
 InputF.send_keys(1000)
 inputC.clear()
 InputF.clear()
 inputC.send_keys(999)
 InputF.send_keys(999)

except Exception as ex:
 print(ex)
finally:
 chrome.quit()
 firefox.quit()