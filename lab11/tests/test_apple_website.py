import sys
import time
from asyncio import exceptions
from os.path import dirname, abspath

sys.path.insert(0, dirname(dirname(abspath(__file__))))
import json
import unittest
from selenium import webdriver
from pages.home_page import AppleHomePage
from pages.iphone_page import IPhonePage
from pages.iphone_model_page import IPhoneModelPage
from pages.shopping_cart_page import ShoppingCartPage


class AppleWebsiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.home_page = AppleHomePage(self.driver)
        self.iphone_page = IPhonePage(self.driver)
        self.iphone_model_page = IPhoneModelPage(self.driver)
        self.shopping_cart_page = ShoppingCartPage(self.driver)

    def test_search(self):
        with open('../data/test_data.json') as f:
            test_data = json.load(f)
        product_name = test_data["product"]
        self.home_page.load()
        self.home_page.click_search_link()
        self.home_page.enter_search_text(product_name)
        find = self.home_page.is_search_results_visible()
        self.assertEqual(find, True, "Элемент не найден")

    def test_open_search(self):
        with open('../data/test_data.json') as f:
            test_data = json.load(f)

        product_name = test_data["product"]
        self.home_page.load()
        self.home_page.click_search_link()
        self.home_page.enter_search_text(product_name)
        self.home_page.click_search_item()
        wall = self.home_page.is_element_wall()

        self.assertEqual(wall, True, "На этой странице нет информации")

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
        self.shopping_cart_page.click_remove_bag_link()

    def test_undo_cart(self):
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
        self.shopping_cart_page.click_remove_bag_link()

    def test_delete_cart(self):
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
        try:
            current_value = self.shopping_cart_page.get_quantity_value()
        except exceptions:
            one = 1
            self.assertEqual(one, '1', "Значение в элементе не равно 1")

    def test_select_product(self):
        self.home_page.load()
        self.home_page.click_products_link()
        self.iphone_page.click_iphone_link()

        wall = self.home_page.is_product_wall()
        self.assertEqual(wall, True, "На этой странице нет информации")

    def test_change_cart_price(self):
        with open('../data/test_data.json') as f:
            test_data = json.load(f)
        quantity = test_data['quantity']
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

        price_before = float(self.shopping_cart_page.get_monthly_price().replace('$', '').replace(',', ''))
        self.shopping_cart_page.select_quantity(quantity)
        time.sleep(2)
        price_after = float(self.shopping_cart_page.get_monthly_price().replace('$', '').replace(',', ''))

        self.assertEqual(price_before * quantity, price_after, "Цена не верна")

    def test_change_color(self):
        self.home_page.load()
        self.home_page.click_products_link()
        self.iphone_page.click_iphone_link()
        self.iphone_model_page.click_buy_link()

        self.iphone_model_page.click_model_link()
        first = self.iphone_model_page.image_obj()
        self.iphone_model_page.click_color_link()
        self.iphone_model_page.click_color_link2()
        time.sleep(3)
        second = self.iphone_model_page.image_obj()

        self.assertEqual(first != second, True, "поменялось")

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    # Создание объекта TestSuite и добавление всех тестовых кейсов
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(AppleWebsiteTest))

    # Создание объекта TextTestRunner и запуск тестов
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Сохранение результатов выполнения тестов в файл
    with open("../reports/test_results.txt", "w") as f:
        f.write(f"Run: {result.testsRun}\n")
        f.write(f"Errors: {len(result.errors)}\n")
        f.write(f"Failures: {len(result.failures)}\n")
        f.write(f"Ignored: {len(result.skipped)}\n")
