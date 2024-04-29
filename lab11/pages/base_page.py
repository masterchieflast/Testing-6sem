import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=10):
        time.sleep(1)
        element = self.wait_for_element(locator, timeout)
        element.click()

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def get_element_attribute(self, locator, attribute, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)
