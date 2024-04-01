import time
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AppleWebsiteTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.apple.com/")  # Переходим на главную страницу Apple.com

    def test_add_to_cart(self):
        driver = self.driver
        try:
            products_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'globalnav-link-iphone')]"))
            )
            products_link.click()

            iphone_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'chapternav-link')]"))
            )
            iphone_link.click()

            buy_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class,'welcome__lockup-cta')]"))
            )
            buy_link.click()

            model_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'rc-dimension-selector-row form-selector')]"))
            )
            model_link.click()

            color_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(@class,'colornav-link rc-dimension-colornav-link rf-bfe-product-dimension-colornav-label')]"))
            )
            color_link.click()

            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(2)  # Пауза в 2 секунды
            storage_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='rc-dimension-selector-row form-selector'])[3]"))
            )
            storage_link.click()

            driver.execute_script("window.scrollBy(0, window.innerHeight);")

            trade_in_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "(//div[@class='rc-dimension-multiple column large-6 small-6 form-selector'])[2]"))
            )
            trade_in_link.click()

            payment_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(@class,'rf-po-bfe-dimension-base-option rf-po-bfe-purchasegroupoption rf-po-bfe-purchasegroupoption-full-width rc-dimension-multiple column large-6 small-6 form-selector')]"))
            )
            payment_link.click()

            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(2)

            operator_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "(//div[@class='rc-dimension-multiple form-selector-threeline column large-4 small-12 form-selector'])[4]"))
            )
            operator_link.click()

            driver.execute_script("window.scrollBy(0, 0.5 * window.innerHeight);")
            time.sleep(2)

            apple_care_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "(//div[@class='form-selector column large-4 small-12 rf-accessory-applecare-fullwidth-option'])[1]"))
            )
            apple_care_link.click()

            driver.execute_script("window.scrollBy(0, window.innerHeight);")
            time.sleep(2)

            bag_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='button button-block']"))
            )
            bag_link.click()

            bag_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='button button-block button-super']"))
            )
            bag_link.click()

            quantity_dropdown = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'rs-quantity-dropdown'))
            )

            # Получаем текущее значение элемента
            print("всё классно, ехууу")
            current_value = quantity_dropdown.get_attribute('value')

            assert current_value == '1', "Значение в элементе не равно 1"

        except NoSuchElementException as e:
            self.fail("Элемент не найден на странице: {}".format(e))
        except Exception as e:
            self.fail("Произошла ошибка: {}".format(e))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
