from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
 chrome.get("http://the-internet.herokuapp.com/login")
 firefox.get("http://the-internet.herokuapp.com/login")

 userC = chrome.find_element(By.ID, "username")
 userC.send_keys('tomsmith')
 userF = firefox.find_element(By.ID, "username")
 userF.send_keys('tomsmith')

 passC = chrome.find_element(By.ID, "password")
 passC.send_keys('SuperSecretPassword!')
 passF = firefox.find_element(By.ID, "password")
 passF.send_keys('SuperSecretPassword!')

 loginC = chrome.find_element(By.CSS_SELECTOR, "#login > button > i").click()
 loginF = firefox.find_element(By.CSS_SELECTOR, "#login > button > i").click()

except Exception as ex:
 print(ex)
finally:
 chrome.quit()
 firefox.quit()