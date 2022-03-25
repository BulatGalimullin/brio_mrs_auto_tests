from .base_page import BasePage
from .locators import *


class LicencesPage(BasePage):

    # CHECKS
    def should_be_managing_licenses_page(self):
        assert "/Licenses" in self.browser.current_url, "Url of the page doesn't contain '/Licences'"
        assert self.is_element_present(*LicensesPageLocators.LICENSES_TABLE), "There is no table with licenses"

    def should_be_add_licenses_button(self):
        assert self.is_element_present(*LicensesPageLocators.ADD_LICENSE_BUTTON), "There is no button to add licenses"

    def should_not_be_add_licenses_button(self):
        assert self.is_not_element_present(*LicensesPageLocators.ADD_LICENSE_BUTTON), "There is a button to add licenses"

