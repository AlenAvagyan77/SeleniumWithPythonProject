from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass


class SearchProductClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locator.LocatoresClass()

    def search_product(self):
        self.logger.add_log("INFO", "Called search_product method")
        searchFildElement = self.find.custom_find(self.locator.searchFildElement)
        searchFildElement.click()

    def input_product(self):
        self.logger.add_log("INFO", "Called input_product method")
        inputProduct = self.find.custom_find(self.locator.inputProduct)
        inputProduct.send_keys("AGV Helmet")

    def click_button(self):
        self.logger.add_log("INFO", "Called click_button method")
        clickButton = self.find.custom_find(self.locator.clickButton)
        clickButton.click()
