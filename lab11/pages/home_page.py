from .base_page import BasePage
from selenium.webdriver.common.by import By

class AppleHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.apple.com/"
        self.products_link = (By.XPATH, "//a[contains(@class,'globalnav-link-iphone')]")

    def load(self):
        self.driver.get(self.url)

    def click_products_link(self):
        self.click_element(self.products_link)
