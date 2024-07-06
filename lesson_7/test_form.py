from configuration import *
from form_pages import MainPage


def test_form(driver):
    main_page = MainPage(driver)
    main_page.first_name('Иван')
    main_page.last_name('Петров')
    main_page.address('Ленина, 55-3')
    main_page.city('Москва')
    main_page.country('Россия')
    main_page.email('test@skypro.com')
    main_page.phone('+7985899998787')
    main_page.job('QA')
    main_page.company('SkyPro')
    main_page.zipcode('')
    main_page.submit()

    to_be_green_elements = 9
    as_is_green_elements = main_page.find_green_elements(to_be_green_elements)
    assert as_is_green_elements == to_be_green_elements

    to_be_red_elements = 1
    as_is_red_elements = main_page.find_red_elements(to_be_red_elements)
    assert as_is_red_elements == to_be_red_elements
