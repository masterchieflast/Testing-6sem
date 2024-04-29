from .base_page import BasePage
from selenium.webdriver.common.by import By

class AppleHomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.apple.com/"
        self.products_link = (By.XPATH, "//a[contains(@class,'globalnav-link-iphone')]")
        self.search_link = (By.XPATH, "//a[contains(@class,'globalnav-link globalnav-link-search')]")
        self.search_item = (By.XPATH, "//a[contains(@class,'globalnav-searchresults-list-link')][1]")
        self.search_input = (By.CLASS_NAME, "globalnav-searchfield-input")
        self.search_results_container = (By.CLASS_NAME, "globalnav-searchresults-container")

    def load(self):
        self.driver.get(self.url)

    def click_products_link(self):
        self.click_element(self.products_link)

    def click_search_link(self):
        self.click_element(self.search_link)
        self.focus_search_input()

    def enter_search_text(self, text):
        search_field = self.wait_for_element(self.search_input)
        search_field.clear()
        search_field.send_keys(text)

    def click_search_item(self):
        self.click_element(self.search_item)

    def focus_search_input(self):
        search_field = self.wait_for_element(self.search_input)
        self.driver.execute_script("arguments[0].focus();", search_field)

    def is_search_results_visible(self):
        return self.is_element_visible(self.search_results_container)