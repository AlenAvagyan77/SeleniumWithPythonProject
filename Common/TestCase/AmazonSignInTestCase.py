from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Common.Pages import SignInPage
from Common.Pages import PasswordPage
from Common.Pages import AmazonMainPage
from Common.Pages import SearchProduct
from Common.Pages import ProductFile
from Common.Variables import Variables
from Common.TestCase.BaseTest import BaseTestClass


class SignIn(BaseTestClass):

    def setUp(self):
        self.logger.add_log("INFO", "_________________________________________________")
        self.logger.add_log("INFO", "Starting Test Case {}".format(type(self).__name__))
        self.logger.add_log("INFO", "_________________________________________________")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.signInPage = SignInPage.InputNumberClass(self.driver)
        self.passwordPage = PasswordPage.InputPasswordClass(self.driver)
        self.MainPage = AmazonMainPage.MainPageClass(self.driver)
        self.searchProduct = SearchProduct.SearchProductClass(self.driver)
        self.productFile = ProductFile.ProductFileClass(self.driver)
        self.variables = Variables.ProjectVariables()
        self.driver.get(self.variables.mainURL)

    def test_myAmazonTest(self):
        self.assertEqual("Amazon.com. Spend less. Smile more.", self.MainPage.get_title(), "ERROR")
        self.signInPage.click_number_line()
        self.signInPage.input_to_number()
        self.signInPage.click_into_continue_button()
        self.passwordPage.click_password_line()
        self.passwordPage.input_password()
        self.passwordPage.press_into_keep_me_check_box()
        self.passwordPage.sign_in_button()
        self.logger.add_log("INFO", "Test Case '{}' Finished".format(type(self).__name__))

    def tearDown(self):
        self.driver.delete_all_cookies()































