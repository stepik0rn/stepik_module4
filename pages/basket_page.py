from .base_page import BasePage
from .locators import BasketLocators

class BasketPage(BasePage):
    def should_be_empty_cart(self):
        assert self.is_not_element_present(*BasketLocators.ITEMS)
        
    def should_be_empty_cart_message(self):
        assert self.is_element_present(*BasketLocators.EMPTY_BASKET_MSG)
    
