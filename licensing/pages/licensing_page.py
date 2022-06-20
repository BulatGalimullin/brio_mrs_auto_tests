from .base_page import BasePage
from .locators import *
import os
import time
import pytest


def latest_download_file(download_path):
    os.chdir(download_path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]
    if os.path.isfile(newest):
        return newest
    else:
        raise ValueError("%s this path didn't contain files!" % download_path)


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
        assert self.is_element_present(
            *LicensesPageLocators.DOWNLOAD_LICENSE_BUTTON), "Not possible to download license file"

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

    def open_add_new_license_page(self):
        self.browser.find_element(*LicensesPageLocators.ADD_LICENSE_BUTTON).click()

    def cancel_adding_new_license(self):
        self.browser.find_element(*LicensesPageLocators.CANCEL_ADD_LICENSE_BUTTON).click()

    def download_license_file(self, path_to_download='default'):
        self.browser.find_element(*LicensesPageLocators.DOWNLOAD_LICENSE_BUTTON).click()
        if path_to_download == 'default':
            self.is_download_finished(pytest.def_download_folder)
        # else:
        # os.chdir()

    def is_download_finished(self, download_path=pytest.def_download_folder):
        download_finished = False
        while download_finished is False:
            time.sleep(0.5)
            newest_file = latest_download_file(download_path)
            if ".crdownload" in newest_file or ".part" in newest_file:
                download_finished = False
            else:
                download_finished = True
        assert download_finished, "File is not downloaded"

