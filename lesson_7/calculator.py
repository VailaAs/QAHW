from configuration import *
from calculator_pages import MainPage


def test_calculator(driver):
    main_page = MainPage(driver)
    main_page.delay_input('45')
    main_page.click_calculator_buttons(['//*[@id="calculator"]/div[2]/span[1]',
                                        '//*[@id="calculator"]/div[2]/span[4]',
                                        '//*[@id="calculator"]/div[2]/span[2]'])

    # for delay copy integer input from delay_input
    main_page.calculation_waiter(15, 45)
