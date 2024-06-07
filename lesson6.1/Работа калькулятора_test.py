from driver import *


def calculator_test(driver_):
    driver_.get(URL_2)
    delay = driver_.find_element(
        By.CSS_SELECTOR, '#delay')
    delay.clear()
    delay.send_keys(45)

    driver_.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[1]').click()
    driver_.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[4]').click()
    driver_.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[2]').click()
    driver_.find_element(
        By.XPATH, '//*[@id="calculator"]/div[2]/span[15]').click()
    WebDriverWait(driver_, 46).until(
        EC.text_to_be_present_in_element(
           (By.XPATH, '//*[@id="calculator"]/div[1]/div'), '15'))
    res = driver_.find_element(
        By.XPATH, '//*[@id="calculator"]/div[1]/div').text
    assert res == '15'


def test_cal_sub(driver_):
    calculator_test(driver_)
