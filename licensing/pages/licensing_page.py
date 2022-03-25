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
        assert self.is_not_element_present(
            *LicensesPageLocators.ADD_LICENSE_BUTTON), "There is a button to add licenses"

    def should_be_the_last_licenses_page(self):
        assert self.browser.find_element(*LicensesPageLocators.LICENSES_PENULTIMATE_PAGE).get_attribute(
            "href") in self.browser.current_url, "This is not the last page"

    def should_be_download_license_button(self):
        assert self.is_element_present(*LicensesPageLocators.DOWNLOAD_LICENSE_BUTTON), "Not possible to download license file"

    def should_be_revoke_button(self):
        assert self.is_element_present(*LicensesPageLocators.REVOKE_BUTTON), "Not possible to revoke license file"

    def should_not_be_revoke_button(self):
        assert self.is_not_element_present(*LicensesPageLocators.REVOKE_BUTTON), "It's possible to revoke license " \
                                                                                 "file. User should not be able to do" \
                                                                                 " that "

    # ACTIONS
    def go_to_the_licenses_page_number(self, number):
        if isinstance(number, str) and number.casefold() == 'first':
            self.browser.find_element(*LicensesPageLocators.FIRST_PAGE).click()
            assert 'page=1' in self.browser.current_url, "This is not first page"
        elif isinstance(number, str) and number.casefold() == 'last':
            self.browser.find_element(*LicensesPageLocators.LAST_PAGE).click()
            self.should_be_the_last_licenses_page()
        elif isinstance(number, int) and number <= 20:
            current_page = self.browser.find_element(*LicensesPageLocators.PAGE_NUMBER[number])
            current_page.click()
            assert F'page={number}' in self.browser.current_url, F"This is not page number {number}"

    def open_license_info_nth_license(self, number):
        self.browser.find_element(*LicensesPageLocators.OPEN_LICENSE_NUMBER[number]).click()
