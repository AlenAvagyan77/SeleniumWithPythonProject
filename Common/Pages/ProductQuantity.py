from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass


class ProductQuantity(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locator.LocatoresClass()

    def click_cart_box(self):
        self.logger.add_log("INFO", "Called click_cart_box method")
        click_cart_box = self.find.custom_find(self.locator.click_cart_box)
        click_cart_box.click()

    def qty_button(self):
        self.logger.add_log("INFO", "Called qty_button method")
        qty_button = self.find.custom_find(self.locator.qty_button)
        qty_button.click()

    def increase_the_number(self):
        self.logger.add_log("INFO", "Called increase_the_number method")
        increase_the_number = self.find.custom_find(self.locator.increase_the_number)
        increase_the_number.click()




