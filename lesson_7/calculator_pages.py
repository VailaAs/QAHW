from configuration import *


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(URL_2)

    def delay_input(self, input):
        delay = self.driver.find_element(
            By.CSS_SELECTOR, '#delay')
        delay.clear()
        delay.send_keys(input)

    def click_calculator_buttons(self, button_XPATHs):
        for button_XPATH in button_XPATHs:
            button = self.driver.find_element(By.XPATH, button_XPATH)
            button.click()
        self.driver.find_element(
            By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()

    def calculation_waiter(self, to_be_result, delay):
        WebDriverWait(self.driver, delay+1).until(
            EC.invisibility_of_element_located((By.ID, 'spinner')))
        screen_element = self.driver.find_element(By.CSS_SELECTOR, '[class="screen"]')
        as_is_res = int(screen_element.text)
        return as_is_res
