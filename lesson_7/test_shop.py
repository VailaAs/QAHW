from configuration import *
from shop_pages import *


def test_shop(driver):
    auth_page = AuthorizationPage(driver)
    auth_page.auth('standard_user')

    main_page = MainPage(driver)
    main_page.add_products(['add-to-cart-sauce-labs-backpack',
                            'add-to-cart-sauce-labs-bolt-t-shirt',
                            'add-to-cart-sauce-labs-onesie'])

    cart_page = CartPage(driver)
    cart_page.checkout_form('Alla', 'Sky', 123456) 
    
    to_be_result = 58.29
    as_is_result = cart_page.check_total_sum(to_be_result)
    assert f'Total: ${to_be_result}' == as_is_result
