from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
 chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
 firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")
 for x in range(5):
  chrome.find_element(
    By.XPATH, '(//*[@id="content"]/div/button)').click() 
  firefox.find_element(
    By.XPATH, '(//*[@id="content"]/div/button)').click()
 del_button_chrome = chrome.find_elements(By.XPATH, '(//*[@id="elements"]/button)')
 del_button_firefox = firefox.find_elements(By.XPATH, '(//*[@id="elements"]/button)')

 print('Размер списка кнопок Chrome:',len(del_button_chrome))
 print('Размер списка кнопок Firefox:',len(del_button_firefox))

except Exception as ex:
 print(ex)
finally:
 chrome.quit()
 firefox.quit()