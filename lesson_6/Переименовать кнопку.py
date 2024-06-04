from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
try:
 driver.get('https://uitestingplayground.com/textinput')
 button_new = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').text
 input = driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys('SkyPro')
 button = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').click()
 button_upd = driver.find_element(By.CSS_SELECTOR, '[class="btn btn-primary"]').text

 print('До:', button_new)
 print('После:', button_upd)

except Exception as ex:
 print(ex)

finally:
 driver.quit()