from .base_page import BasePage
from selenium.webdriver.common.by import By


class IPhoneModelPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.buy_link = (By.XPATH, "//a[contains(@class,'welcome__lockup-cta')]")
        self.model_link = (By.XPATH, "//div[contains(@class,'rc-dimension-selector-row form-selector')]")
        self.color_link = (By.XPATH,
                           "//label[contains(@class,'colornav-link rc-dimension-colornav-link "
                           "rf-bfe-product-dimension-colornav-label')]")
        self.color_link = (By.XPATH,
                           "//label[contains(@class,'colornav-link rc-dimension-colornav-link "
                           "rf-bfe-product-dimension-colornav-label')]")
        self.color_link2 = (By.XPATH,
                            "(//label[contains(@class,'colornav-link rc-dimension-colornav-link "
                            "rf-bfe-product-dimension-colornav-label')])[3]")
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
        self.image_wrapper = (By.CLASS_NAME, 'rf-bfe-gallery-image-wrapper')

    def click_buy_link(self):
        self.click_element(self.buy_link)

    def click_model_link(self):
        self.click_element(self.model_link)
        self.wait_for_element_to_be_clickable(self.model_link)

    def click_color_link(self):
        self.click_element(self.color_link)
        self.wait_for_element_to_be_clickable(self.color_link)

    def click_color_link2(self):
        self.click_element(self.color_link2)
        self.wait_for_element_to_be_clickable(self.color_link2)

    def click_storage_link(self):
        self.click_element(self.storage_link)
        self.wait_for_element_to_be_clickable(self.storage_link)

    def click_trade_in_link(self):
        self.click_element(self.trade_in_link)
        self.wait_for_element_to_be_clickable(self.trade_in_link)

    def click_payment_link(self):
        self.click_element(self.payment_link)
        self.wait_for_element_to_be_clickable(self.payment_link)

    def click_operator_link(self):
        self.click_element(self.operator_link)
        self.wait_for_element_to_be_clickable(self.operator_link)

    def click_apple_care_link(self):
        self.click_element(self.apple_care_link)
        self.wait_for_element_to_be_clickable(self.apple_care_link)

    def click_bug_link(self):
        self.wait_for_element_to_be_clickable(self.bug_link)
        self.click_element(self.bug_link)

    def click_renew_bug_link(self):
        self.wait_for_element_to_be_clickable(self.renew_bug_link)
        self.click_element(self.renew_bug_link)

    def image_obj(self):
        return self.wait_for_element(self.image_wrapper)
