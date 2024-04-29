from .base_page import BasePage
from selenium.webdriver.common.by import By


class IPhonePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.iphone_link = (By.XPATH, "//a[contains(@class,'chapternav-link')]")

    def click_iphone_link(self):
        self.click_element(self.iphone_link)
