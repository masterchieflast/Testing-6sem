from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class IPhonePage:
    def __init__(self, driver):
        self.driver = driver
        self.iphone_link = (By.XPATH, "//a[contains(@class,'chapternav-link')]")

    def click_iphone_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.iphone_link)).click()
