from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
# browser = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

try:
 browser.get("http://the-internet.herokuapp.com/add_remove_elements/")
 for x in range(5):
  browser.find_element(
    By.XPATH, '(//*[@id="content"]/div/button)').click()
 del_button = browser.find_elements(By.XPATH, '(//*[@id="elements"]/button)')

 print('Размер списка кнопок:',len(del_button))

except Exception as ex:
 print(ex)
finally:
 browser.quit()