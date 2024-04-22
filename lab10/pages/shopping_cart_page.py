from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.remove_bag_link = (By.XPATH, "//button[@class='rs-iteminfo-remove as-buttonlink']")
        self.undo_bag_link = (By.XPATH, "//button[@class='as-buttonlink'][1]")
        self.quantity_dropdown = (By.CLASS_NAME, 'rs-quantity-dropdown')

    def click_remove_bag_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.remove_bag_link)).click()

    def click_undo_bag_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.undo_bag_link)).click()

    def get_quantity_value(self):
        quantity_dropdown = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.quantity_dropdown))
        return quantity_dropdown.get_attribute('value')
