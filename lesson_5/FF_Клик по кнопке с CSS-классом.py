from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    firefox.get("https://uitestingplayground.com/classattr")
    count = 0
    for _ in range(3):
        firefox.find_element(
            By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
        count += 1
        firefox.switch_to.alert.accept()

    print(f'Кнопка Firefox нажата {count} раза')

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
