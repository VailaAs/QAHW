from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install())) 

# --ctrl+/--- для смены на Firefox

try:
 browser.get("http://the-internet.herokuapp.com/login")
 user = browser.find_element(By.ID, "username")
 user.send_keys('tomsmith')
 pass_ = browser.find_element(By.ID, "password")
 pass_.send_keys('SuperSecretPassword!')
 login = browser.find_element(By.CSS_SELECTOR, "#login > button > i").click()

except Exception as ex:
 print(ex)
finally:
 browser.quit()