from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass

class ShoppingCartClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locator.LocatoresClass()

    def delete_first_product_from_cart(self):
        self.logger.add_log("INFO", "Called delete_first_product_from_cart method")
        deleteFirstProduct = self.find.custom_find(self.locator.deleteFirstProduct)
        deleteFirstProduct.click()
