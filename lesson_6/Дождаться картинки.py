from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
 driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
 waiter = WebDriverWait(driver, 30)
 waiter.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[class="lead"]'), 'Done!')
 )
 txt = driver.find_element(By.CSS_SELECTOR, '#award').get_attribute('src')

 print('Текст 3 картинки:', txt)
 

except Exception as ex:
 print(ex)

finally:
 driver.quit()