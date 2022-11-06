from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CART_LINK = (By.CSS_SELECTOR, "div.basket-mini a.btn-default")

class BasketLocators:
    ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MSG = (By.CSS_SELECTOR, "#content_inner p")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "div.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "div.register_form")

    
class ProductPageLocators:
    BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "article.product_page div.product_main h1")
    ALERT_SUCCESS = (By.CSS_SELECTOR, "div.alert-success")
    ADD_NOTIFICATION = (By.CSS_SELECTOR, "div.alert-success:nth-child(1)")
    PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
    PRICE_NOTIFICATION = (By.XPATH, "//div[contains(@class, 'alert-info')]//p[1]")
