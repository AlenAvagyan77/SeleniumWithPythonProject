from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass


class SignOutClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locator.LocatoresClass()

    def all_section(self):
        self.logger.add_log("INFO", "Called all_section method")
        all_button = self.find.custom_find(self.locator.all_button)
        all_button.click()

    def sign_out(self):
        self.logger.add_log("INFO", "Called sign_out method")
        sign_out_button = self.find.custom_find(self.locator.sign_out_button)
        sign_out_button.click()





