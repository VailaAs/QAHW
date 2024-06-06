from driver import *


def shop_test(driver_):
    driver_.get(URL_3)
    # login
    driver_.find_element(
        By.ID, 'user-name').send_keys('standard_user')
    driver_.find_element(
        By.ID, 'password').send_keys('secret_sauce')
    driver_.find_element(
        By.ID, 'login-button').click()
    # add products to cart
    driver_.find_element(
        By.ID, 'add-to-cart-sauce-labs-backpack').click()
    driver_.find_element(
        By.ID, 'add-to-cart-sauce-labs-bolt-t-shirt').click()
    driver_.find_element(
        By.ID, 'add-to-cart-sauce-labs-onesie').click()
    # go to cart
    driver_.find_element(
        By.CSS_SELECTOR, '[class="shopping_cart_link"]').click()
    # click checkout
    driver_.find_element(
        By.ID, 'checkout').click()
    # fill in the checkout form
    driver_.find_element(
        By.ID, 'first-name').send_keys('AL')
    driver_.find_element(
        By.ID, 'last-name').send_keys('PY')
    driver_.find_element(
        By.ID, 'postal-code').send_keys('123456')
    driver_.find_element(
        By.ID, 'continue').click()
    # check total sum
    total = driver_.find_element(
        By.CSS_SELECTOR, '[data-test="total-label"]').text
    assert total == 'Total: $58.29'


def test_shop_sub(driver_):
    shop_test(driver_)
