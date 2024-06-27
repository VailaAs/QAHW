from configuration import *


class MainPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(URL_1)

    def first_name(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="first-name"]').send_keys(input)

    def last_name(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="last-name"]').send_keys(input)

    def address(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="address"]').send_keys(input)

    def city(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="city"]').send_keys(input)

    def country(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="country"]').send_keys(input)

    def email(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="e-mail"]').send_keys(input)

    def phone(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="phone"]').send_keys(input)

    def job(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="job-position"]').send_keys(input)

    def company(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="company"]').send_keys(input)

    def zipcode(self, input):
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="zip-code"]').send_keys(input)

    def submit(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '[type="submit"]'))).click()

    def find_green_elements(self, to_be_elements):
        green = self.driver.find_elements(
            By.CSS_SELECTOR, '[class="alert py-2 alert-success"]')
        return len(green)

    def find_red_elements(self, to_be_elements):
        red = self.driver.find_elements(
            By.CSS_SELECTOR, '[class="alert py-2 alert-danger"]')
        return len(red)
