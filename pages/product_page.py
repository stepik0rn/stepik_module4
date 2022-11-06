from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_add2cart_btn()
        product = self.should_be_product_name()
        price = self.should_be_price()
        return product, price
    
    def put_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET).click()
        
    def should_be_add2cart_btn(self):
        self.is_element_present(*ProductPageLocators.BASKET)
    
    def shoud_be_notified(self, product, price):
        self.is_element_present(*ProductPageLocators.ADD_NOTIFICATION)
        self.should_be_product_name_notification(product)
        self.should_be_price_notification(price)
        
    def should_be_product_name_notification(self, product):
        # p_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        add_notification = self.browser.find_element(*ProductPageLocators.ADD_NOTIFICATION)
        n_pname = add_notification.find_element(By.XPATH, ".//strong").text
        assert n_pname == product, f"Expected '{product}' in notification, got {n_pname}"
        
    def should_be_product_name(self):
        return self.is_element_present(*ProductPageLocators.PRODUCT_NAME).text
        
    def should_be_price(self):
        return self.is_element_present(*ProductPageLocators.PRICE).text
    
    def should_be_price_notification(self, price):
        price_in_not_text = self.browser.find_element(*ProductPageLocators.PRICE_NOTIFICATION).text.rsplit(maxsplit=1)[1]
        assert price_in_not_text == price, f"Expected price '{price}', got '{price_in_not_text}'"
    
    def should_not_be_success_message(self):
        self.is_not_element_present(*ProductPageLocators.ADD_NOTIFICATION)
