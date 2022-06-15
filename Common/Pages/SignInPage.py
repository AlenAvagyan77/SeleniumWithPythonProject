from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass


class InputNumberClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locator.LocatoresClass()

    def click_number_line(self):
        self.logger.add_log("INFO", "Called click_number_line method")
        clickSignInButton = self.find.custom_find(self.locator.clickSignInSection)
        clickSignInButton.click()

    def input_to_number(self):
        self.logger.add_log("INFO", "Called input_to_number method")
        inputNumber = self.find.custom_find(self.locator.clickSignInButton)
        inputNumber.send_keys("043444255")

    def click_into_continue_button(self):
        self.logger.add_log("INFO", "Called click_into_continue_button method")
        clickIntoContinueButton = self.find.custom_find(self.locator.ContinueButton)
        clickIntoContinueButton.click()











