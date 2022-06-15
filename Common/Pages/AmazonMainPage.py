from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass

class MainPageClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = Locator.LocatoresClass()

    def fill_search_field(self):
        self.logger.add_log("INFO", "Called fill_search_field method")
        searchField = self.find.custom_find(self.locators)
        searchField.click()

    def press_to_search_button(self):
        self.logger.add_log("INFO", "Called press_to_search_button method")
        amazonSignInButton = self.driver.find_element(self.locators)
        amazonSignInButton.click()