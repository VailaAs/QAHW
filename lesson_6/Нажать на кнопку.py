from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get('https://uitestingplayground.com/ajax')
    driver.find_element(
        By.CSS_SELECTOR, '#ajaxButton').click()

    waiter = WebDriverWait(driver, 20)
    ajax = waiter.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '[class="bg-success"]'))
    )
    txt = ajax.text

    print('Текст загруженного элемента:', txt)

except Exception as ex:
    print(ex)

finally:
    driver.quit()
