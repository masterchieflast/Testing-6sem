import sys
from os.path import dirname, abspath
sys.path.insert(0, dirname(dirname(abspath(__file__))))
import unittest
from selenium import webdriver
from pages.home_page import AppleHomePage
from pages.iphone_page import IPhonePage
from pages.iphone_model_page import IPhoneModelPage
from pages.shopping_cart_page import ShoppingCartPage
import json


class AppleWebsiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.home_page = AppleHomePage(self.driver)
        self.iphone_page = IPhonePage(self.driver)
        self.iphone_model_page = IPhoneModelPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)

    def test_add_to_cart(self):

        self.home_page.load()
        self.home_page.click_products_link()
        self.iphone_page.click_iphone_link()
        self.iphone_model_page.click_buy_link()

        self.iphone_model_page.click_model_link()
        self.iphone_model_page.click_color_link()
        self.iphone_model_page.click_storage_link()
        self.iphone_model_page.click_trade_in_link()
        self.iphone_model_page.click_payment_link()
        self.iphone_model_page.click_operator_link()
        self.iphone_model_page.click_apple_care_link()
        self.iphone_model_page.click_bug_link()
        self.iphone_model_page.click_renew_bug_link()

        current_value = self.shopping_cart_page.get_quantity_value()
        self.assertEqual(current_value, '1', "Значение в элементе не равно 1")

    def test_undo_cart(self):
        # with open('../data/test_data.json') as f:
        #     test_data = json.load(f)
        #
        # product_name = test_data["product"]

        self.home_page.load()
        self.home_page.click_products_link()
        self.iphone_page.click_iphone_link()
        self.iphone_model_page.click_buy_link()

        self.iphone_model_page.click_model_link()
        self.iphone_model_page.click_color_link()
        self.iphone_model_page.click_storage_link()
        self.iphone_model_page.click_trade_in_link()
        self.iphone_model_page.click_payment_link()
        self.iphone_model_page.click_operator_link()
        self.iphone_model_page.click_apple_care_link()
        self.iphone_model_page.click_bug_link()
        self.iphone_model_page.click_renew_bug_link()

        self.shopping_cart_page.click_remove_bag_link()
        self.shopping_cart_page.click_undo_bag_link()

        current_value = self.shopping_cart_page.get_quantity_value()
        self.assertEqual(current_value, '1', "Значение в элементе не равно 1")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
