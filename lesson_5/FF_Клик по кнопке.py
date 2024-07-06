from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

firefox = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install()))

try:
    firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")
    for _ in range(5):
        firefox.find_element(
            By.XPATH, '(//*[@id="content"]/div/button)').click()
    del_button = firefox.find_elements(
        By.XPATH, '(//*[@id="elements"]/button)')

    print(f'Размер списка кнопок Firefox: {len(del_button)}')

except Exception as ex:
    print(ex)
finally:
    firefox.quit()
