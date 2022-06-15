import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Common.Pages import SignInPage
from Common.Pages import PasswordPage
from Common.Pages import AmazonMainPage
from Common.Pages import SearchProduct
from Common.Pages import ProductFile
from Common.Pages import CartSectionPage
from Common.Pages import ChangeName
from Common.Pages import ProductQuantity
from Common.Variables import Variables
from Common.TestCase.BaseTest import BaseTestClass


class AddQuantityProducts(BaseTestClass):

    def setUp(self):
        self.logger.add_log("INFO", "_________________________________________________")
        self.logger.add_log("INFO", "Starting Test Case {}".format(type(self).__name__))
        self.logger.add_log("INFO", "_________________________________________________")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.SignInPage = SignInPage.InputNumberClass(self.driver)
        self.PasswordPage = PasswordPage.InputPasswordClass(self.driver)
        self.MainPage = AmazonMainPage.MainPageClass(self.driver)
        self.SearchProduct = SearchProduct.SearchProductClass(self.driver)
        self.ProductFile = ProductFile.ProductFileClass(self.driver)
        self.SearchProduct = SearchProduct.SearchProductClass(self.driver)
        self.ProductFile = ProductFile.ProductFileClass(self.driver)
        self.CartSection = CartSectionPage.ShoppingCartClass(self.driver)
        self.ChangeName = ChangeName.ChangeNameClass(self.driver)
        self.ProductQuantity = ProductQuantity.ProductQuantity(self.driver)
        self.variables = Variables.ProjectVariables()
        self.driver.get(self.variables.mainURL)

    def test_myAmazonTest(self):
        self.assertEqual("Amazon.com. Spend less. Smile more.", self.MainPage.get_title(), "ERROR")
        self.SignInPage.click_number_line()
        self.SignInPage.input_to_number()
        self.SignInPage.click_into_continue_button()
        self.PasswordPage.click_password_line()
        self.PasswordPage.input_password()
        self.PasswordPage.press_into_keep_me_check_box()
        self.PasswordPage.sign_in_button()
        self.SearchProduct.search_product()
        self.SearchProduct.input_product()
        self.SearchProduct.click_button()
        self.ProductFile.click_on_the_product()
        self.ProductFile.click_add_to_cart()
        self.ProductQuantity.click_cart_box()
        self.ProductQuantity.qty_button()
        self.ProductQuantity.increase_the_number()
        time.sleep(1)
        self.CartSection.delete_first_product_from_cart()
        self.ChangeName.account_section()
        self.ChangeName.your_account()
        self.ChangeName.my_name()
        self.ChangeName.my_name_details()
        self.ChangeName.edit_section()
        self.ChangeName.add_new_name()
        self.ChangeName.save_new_name()
        self.logger.add_log("INFO", "Test Case '{}' Finished".format(type(self).__name__))

    def tearDown(self):
        self.driver.delete_all_cookies()
