from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage


class ShoppingCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.remove_bag_link = (By.XPATH, "//button[@class='rs-iteminfo-remove as-buttonlink']")
        self.undo_bag_link = (By.XPATH, "//button[@class='as-buttonlink'][1]")
        self.quantity_dropdown = (By.CLASS_NAME, 'rs-quantity-dropdown')
        self.quantity_dropdown2 = (By.XPATH, "//select[@class='rs-quantity-dropdown form-dropdown-select']")
        self.price_element = (By.CSS_SELECTOR, 'div[data-autom="Monthly_price"]')

    def click_remove_bag_link(self):
        self.click_element(self.remove_bag_link)

    def click_undo_bag_link(self):
        self.click_element(self.undo_bag_link)

    def get_quantity_value(self):
        return self.get_element_attribute(self.quantity_dropdown, 'value')

    def select_quantity(self, value):
        dropdown = Select(self.wait_for_element(self.quantity_dropdown2))
        dropdown.select_by_value(str(value))

    def get_quantity_value(self):
        return self.get_element_attribute(self.quantity_dropdown2, 'value')

    def get_monthly_price(self):
        price_element = self.wait_for_element(self.price_element)
        return price_element.text