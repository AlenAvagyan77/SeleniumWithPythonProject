import names
from Common.Locator import Locator
from Common.Pages.BasePage import BasePageClass


class ChangeNameClass(BasePageClass):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = Locator.LocatoresClass()

    def account_section(self):
        self.logger.add_log("INFO", "Called account_section method")
        return_Account = self.find.custom_find(self.locator.return_Account)
        return_Account.click()

    def your_account(self):
        self.logger.add_log("INFO", "Called your_account method")
        your_Account = self.find.custom_find(self.locator.your_Account)
        your_Account.click()

    def my_name(self):
        self.logger.add_log("INFO", "Called my_name method")
        my_name = self.find.custom_find(self.locator.my_name)
        my_name.click()

    def my_name_details(self):
        self.logger.add_log("INFO", "Called my_name_details method")
        my_name_details = self.find.custom_find(self.locator.my_name_details)
        my_name_details.click()

    def edit_section(self):
        self.logger.add_log("INFO", "Called edit_section method")
        edit_section = self.find.custom_find(self.locator.edit_section)
        edit_section.click()
        edit_section.clear()

    def add_new_name(self):
        self.logger.add_log("INFO", "Called add_new_name method")
        edit_section = self.find.custom_find(self.locator.edit_section)
        edit_section.send_keys(names.get_full_name(gender='male'))

    def save_new_name(self):
        self.logger.add_log("INFO", "Called save_new_name method")
        save_changes = self.find.custom_find(self.locator.save_changes)
        save_changes.click()




