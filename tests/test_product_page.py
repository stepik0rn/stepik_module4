from ..pages.product_page import ProductPage
from ..pages.main_page import MainPage
from ..pages.login_page import LoginPage
from ..pages.basket_page import BasketPage
from ..pages.locators import ProductPageLocators
from pytest import mark, param, fixture
from time import sleep, time

PROD_PAGE_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

class TestUserAddToBasketFromProductPage:

    @fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = ProductPage(browser, PROD_PAGE_LINK)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.register_new_user(str(time()) + "@fakemail.org", "VerySecurePassword")
        login_page.should_be_authorized_user()

        
    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PROD_PAGE_LINK)
        page.open()
        page.should_not_be_success_message()
    
    @mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = MainPage(browser, PROD_PAGE_LINK)
        page.open()
        prod_page = ProductPage(browser, browser.current_url)
        product, price = prod_page.should_be_product_page()
        prod_page.put_to_basket()
        prod_page.shoud_be_notified(product, price)


@mark.need_review
@mark.parametrize("promo", [
    *range(0, 7),
    param(7, marks=mark.xfail(reason="Bug that is not gonna be fixed")),
    8, 9
    ])
def test_guest_can_add_product_to_basket(browser, promo):
    link = PROD_PAGE_LINK + "?promo=offer{promo}"
    page = MainPage(browser, link)
    page.open()
    prod_page = ProductPage(browser, browser.current_url)
    product, price = prod_page.should_be_product_page()
    prod_page.put_to_basket()
    page.solve_quiz_and_get_code()
    prod_page.shoud_be_notified(product, price)


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, PROD_PAGE_LINK)
    page.open()
    prod_page = ProductPage(browser, browser.current_url)
    prod_page.put_to_basket()
    assert page.is_not_element_present(*ProductPageLocators.ALERT_SUCCESS)


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, PROD_PAGE_LINK)
    page.open()
    prod_page = ProductPage(browser, browser.current_url)
    prod_page.put_to_basket()
    assert page.is_disappeared(*ProductPageLocators.ALERT_SUCCESS)

    
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.view_cart()
    basket = BasketPage(browser, browser.current_url)
    basket.should_be_empty_cart()
    basket.should_be_empty_cart_message()




