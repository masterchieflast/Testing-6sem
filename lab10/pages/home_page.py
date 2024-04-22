from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class AppleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.apple.com/"
        self.products_link = (By.XPATH, "//a[contains(@class,'globalnav-link-iphone')]")

    def load(self):
        self.driver.get(self.url)

    def click_products_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.products_link)).click()
