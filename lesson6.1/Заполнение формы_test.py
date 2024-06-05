from driver import *


def form_test(driver_):
    driver_.get(URL_1)
    driver_.find_element(
        By.CSS_SELECTOR, '[name="first-name"]').send_keys('Иван')
    driver_.find_element(
        By.CSS_SELECTOR, '[name="last-name"]').send_keys('Петров')
    driver_.find_element(
        By.CSS_SELECTOR, '[name="address"]').send_keys('Ленина, 55-3')
    driver_.find_element(
        By.CSS_SELECTOR, '[name="city"]').send_keys('Москва')
    driver_.find_element(
        By.CSS_SELECTOR, '[name="country"]').send_keys('Россия')
    driver_.find_element(
        By.CSS_SELECTOR, '[name="e-mail"]').send_keys('test@skypro.com')
    driver_.find_element(
        By.CSS_SELECTOR, '[name="phone"]').send_keys('+7985899998787')
    driver_.find_element(
        By.CSS_SELECTOR, '[name="job-position"]').send_keys('QA')
    driver_.find_element(
        By.CSS_SELECTOR, '[name="company"]').send_keys('SkyPro')

    WebDriverWait(driver_, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, '[type="submit"]'))).click()
    green = driver_.find_elements(
        By.CSS_SELECTOR, '[class="alert py-2 alert-success"]')
    red = driver_.find_element(
        By.ID, 'zip-code')
    assert red.get_attribute('class') == 'alert py-2 alert-danger'
    assert len(green) == 9


def test_form_submission(driver_):
    form_test(driver_)
