from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

try:
    chrome.get("http://the-internet.herokuapp.com/add_remove_elements/")
    for _ in range(5):
        chrome.find_element(
            By.XPATH, '(//*[@id="content"]/div/button)').click()
    del_button = chrome.find_elements(
        By.XPATH, '(//*[@id="elements"]/button)')

    print(f'Размер списка кнопок Chrome: {len(del_button)}')

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
