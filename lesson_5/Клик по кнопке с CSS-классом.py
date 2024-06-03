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
 chrome.get("https://uitestingplayground.com/classattr")
 firefox.get("https://uitestingplayground.com/classattr")
 countC = 0
 countF = 0
 for x in range(3):
  chrome.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
  countC = countC+1
  chrome.switch_to.alert.accept()
  firefox.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
  countF = countF+1
  firefox.switch_to.alert.accept()

 print(f'Кнопка Chrome нажата {countC} раза')  
 print(f'Кнопка Firefox нажата {countF} раза') 

except Exception as ex:
 print(ex)
finally:
 chrome.quit()
 firefox.quit()