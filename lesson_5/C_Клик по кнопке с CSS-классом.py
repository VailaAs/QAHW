from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()))

try:
    chrome.get("https://uitestingplayground.com/classattr")
    count = 0
    for _ in range(3):
        chrome.find_element(
            By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
        count += 1
        chrome.switch_to.alert.accept()

    print(f'Кнопка Chrome нажата {count} раза')

except Exception as ex:
    print(ex)
finally:
    chrome.quit()
