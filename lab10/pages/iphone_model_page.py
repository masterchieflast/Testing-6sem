import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class IPhoneModelPage:
    def __init__(self, driver):
        self.driver = driver
        self.buy_link = (By.XPATH, "//a[contains(@class,'welcome__lockup-cta')]")
        self.model_link = (By.XPATH, "//div[contains(@class,'rc-dimension-selector-row form-selector')]")
        self.color_link = (By.XPATH,
                           "//label[contains(@class,'colornav-link rc-dimension-colornav-link "
                           "rf-bfe-product-dimension-colornav-label')]")
        self.storage_link = (By.XPATH, "(//div[@class='rc-dimension-selector-row form-selector'])[3]")
        self.trade_in_link = (
            By.XPATH, "(//div[@class='rc-dimension-multiple column large-6 small-6 form-selector'])[2]")
        self.payment_link = (By.XPATH,
                             "//div[contains(@class,'rf-po-bfe-dimension-base-option rf-po-bfe-purchasegroupoption "
                             "rf-po-bfe-purchasegroupoption-full-width rc-dimension-multiple column large-6 small-6 "
                             "form-selector')]")
        self.operator_link = (By.XPATH,
                              "(//div[@class='rc-dimension-multiple form-selector-threeline column large-4 small-12 "
                              "form-selector'])[4]")
        self.apple_care_link = (
            By.XPATH,
            "(//div[@class='form-selector column large-4 small-12 rf-accessory-applecare-fullwidth-option'])[1]")
        self.bug_link = (By.XPATH, "//button[@class='button button-block']")
        self.renew_bug_link = (By.XPATH, "//button[@class='button button-block button-super']")

    def click_buy_link(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.buy_link)).click()

    def click_model_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.model_link)).click()

    def click_color_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.color_link)).click()

    def click_storage_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.storage_link)).click()

    def click_trade_in_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.trade_in_link)).click()

    def click_payment_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.payment_link)).click()

    def click_operator_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.operator_link)).click()

    def click_apple_care_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.apple_care_link)).click()

    def click_bug_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.bug_link)).click()

    def click_renew_bug_link(self):
        time.sleep(2)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.renew_bug_link)).click()
