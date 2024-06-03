from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
 chrome.get('https://uitestingplayground.com/dynamicid')
 firefox.get('https://uitestingplayground.com/dynamicid')
 chrome.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']").click()
 firefox.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']").click()

 countC = 0
 countF = 0
 for x in range(3):
  chrome.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']").click()
  countC = countC+1
  firefox.find_element(By.XPATH, "//button[text()='Button with Dynamic ID']").click()
  countF = countF+1

 print(f'Кнопка Chrome нажата {countC} раза')  
 print(f'Кнопка Firefox нажата {countF} раза') 

except Exception as ex:
 print(ex)
finally:
 chrome.quit()
 firefox.quit()