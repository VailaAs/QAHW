from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import pytest

URL_1 = 'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
URL_2 = 'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
URL_3 = 'https://www.saucedemo.com'


@pytest.fixture()
def driver_():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

# pytest lesson6.1   в терминал для пробега тестов
