from selenium.webdriver.common.by import By
from .base_page import BasePage


class ShoppingCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.remove_bag_link = (By.XPATH, "//button[@class='rs-iteminfo-remove as-buttonlink']")
        self.undo_bag_link = (By.XPATH, "//button[@class='as-buttonlink'][1]")
        self.quantity_dropdown = (By.CLASS_NAME, 'rs-quantity-dropdown')

    def click_remove_bag_link(self):
        self.click_element(self.remove_bag_link)

    def click_undo_bag_link(self):
        self.click_element(self.undo_bag_link)

    def get_quantity_value(self):
        return self.get_element_attribute(self.quantity_dropdown, 'value')
