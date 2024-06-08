from configuration import *
from time import sleep
import re


class AuthorizationPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(URL_3)

    def auth(self, login):
        self.driver.find_element(By.ID, 'user-name').send_keys(login)
        self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
        self.driver.find_element(By.ID, 'login-button').click()


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    def add_products(self, products_ids):
        for product_id in products_ids:
            product = self.driver.find_element(By.ID, product_id)
            product.click()


class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(URL_3_cart)

    def checkout_form(self, first_name, last_name, postcode):
        self.driver.find_element(By.ID, 'checkout').click()
        self.driver.find_element(By.ID, 'first-name').send_keys(first_name)
        self.driver.find_element(By.ID, 'last-name').send_keys(last_name)
        self.driver.find_element(By.ID, 'postal-code').send_keys(postcode)
        self.driver.find_element(By.ID, 'continue').click()

    def check_total_sum(self):
        total_element = self.driver.find_element(By.CSS_SELECTOR, '[class="summary_total_label"]')
        total_text = total_element.text
        print(total_text)
