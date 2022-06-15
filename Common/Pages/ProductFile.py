from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass


class ProductFileClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locator.LocatoresClass()

    def click_on_the_product(self):
        self.logger.add_log("INFO", "Called click_on_the_product method")
        clickLink = self.find.custom_find(self.locator.clickLink)
        clickLink.click()

    def click_add_to_cart(self):
        self.logger.add_log("INFO", "Called click_add_to_cart method")
        clickAddToCart = self.find.custom_find(self.locator.clickAddToCart)
        clickAddToCart.click()

