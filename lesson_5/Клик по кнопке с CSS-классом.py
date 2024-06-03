from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
 browser.get("https://uitestingplayground.com/classattr")
 count = 0
 for x in range(3):
  browser.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
  count = count + 1
  browser.switch_to.alert.accept()

 print(f'Кнопка нажата {count} раза') 

except Exception as ex:
 print(ex)
finally:
 browser.quit()