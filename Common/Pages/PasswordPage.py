from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass


class InputPasswordClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locator.LocatoresClass()

    def click_password_line(self):
        self.logger.add_log("INFO", "Called click_password_linen method")
        clickPasswordLine = self.find.custom_find(self.locator.clickPasswordLine)
        clickPasswordLine.click()

    def input_password(self):
        self.logger.add_log("INFO", "Called input_password method")
        clickPasswordLine = self.find.custom_find(self.locator.clickPasswordLine)
        clickPasswordLine.send_keys("043444255")

    def press_into_keep_me_check_box(self):
        self.logger.add_log("INFO", "Called press_into_keep_me_check_box method")
        checkBox = self.find.custom_find(self.locator.checkBox)
        checkBox.click()

    def sign_in_button(self):
        self.logger.add_log("INFO", "Called sign_in_button method")
        clickIntoSignInButton = self.find.custom_find(self.locator.clickIntoSignInButton)
        clickIntoSignInButton.click()








