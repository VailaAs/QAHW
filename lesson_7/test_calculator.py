from configuration import *
from calculator_pages import MainPage


def test_calculator(driver):
    main_page = MainPage(driver)
    delay = 45
    main_page.delay_input(str(delay))
    main_page.click_calculator_buttons(['//*[@id="calculator"]/div[2]/span[1]',
                                        '//*[@id="calculator"]/div[2]/span[4]',
                                        '//*[@id="calculator"]/div[2]/span[2]'])
    
    to_be_result = 15
    as_is_result = main_page.calculation_waiter(to_be_result, delay)
    assert as_is_result == to_be_result
