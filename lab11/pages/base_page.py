import json
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    with open('../data/test_data.json') as f:
        test_data = json.load(f)
    timeout = test_data['timeout']

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator, timeout=timeout):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def click_element(self, locator, timeout=timeout):
        time.sleep(1)
        element = self.wait_for_element(locator, timeout)
        element.click()

    def wait_for_element_to_be_clickable(self, locator, timeout=timeout):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def get_element_attribute(self, locator, attribute, timeout=timeout):
        element = self.wait_for_element(locator, timeout)
        return element.get_attribute(attribute)

    def is_element_visible(self, locator, timeout=timeout):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_element_wall(self, timeout=timeout):
        locator = (By.CLASS_NAME, "section-content")
        try:
            for i in range(3):
                self.driver.execute_script("window.scrollBy(0, window.innerHeight);")
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def is_product_wall(self, timeout=timeout):
        locator = (By.XPATH, "//div[contains(@class,'welcome welcome-avail')]")
        try:
            self.driver.execute_script("window.scrollBy(0, window.innerHeight * 0.1);")
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False