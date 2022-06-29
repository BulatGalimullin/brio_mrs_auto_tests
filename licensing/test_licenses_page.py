import pytest

from .pages.licensing_page import LicencesPage
from .pages.login_page import LoginPage
from .pages.main_page import MainPage

base_link = "https://licensing.briogroup.ru"
zzz_test_link = '/Licenses?userId=97de743a-8a8a-4524-bef9-2fdc12f144de'


class TestLicencesPagesAsUser:

    @pytest.fixture(scope='function', autouse=True)
    def login_as_user(self, browser):
        self.link = base_link
        self.page = MainPage(browser, self.link)
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.login('zzz_test', 'Qwe1234!')
        self.login_page.should_be_authorized_user()

    @pytest.mark.parametrize("list_number", ["last", "first", 1, 2])
    def test_user_can_change_licenses_page_with_buttons(self, browser, list_number):
        link = base_link + zzz_test_link
        licenses_page = LicencesPage(browser, link)
        licenses_page.go_to_the_licenses_page_number(list_number)
        licenses_page.should_be_managing_licenses_page()
        licenses_page.should_not_be_add_licenses_button()

    def test_user_can_view_own_licenses(self, browser):
        link = base_link + zzz_test_link
        licenses_page = LicencesPage(browser, link)
        licenses_page.open_license_info_nth_license(1)
        licenses_page.should_be_download_license_button()
        licenses_page.should_not_be_revoke_button()


class TestLicencesPagesAsAdmin:

    @pytest.fixture(scope='function', autouse=True)
    def login_as_admin(self, browser):
        self.link = base_link
        self.page = MainPage(browser, self.link)
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.login('admin', 'Qwe123!')
        self.login_page.should_be_authorized_user()

    @pytest.mark.parametrize("list_number", ["last", "first", 1, 2])
    def test_admin_can_change_licenses_page_with_buttons(self, browser, list_number):
        link = base_link + zzz_test_link
        licenses_page = LicencesPage(browser, link)
        licenses_page.go_to_the_licenses_page_number(list_number)
        licenses_page.should_be_managing_licenses_page()
        licenses_page.should_be_add_licenses_button()

    def test_admin_can_open_licenses_of_user(self, browser):
        link = base_link + zzz_test_link
        licenses_page = LicencesPage(browser, link)
        licenses_page.open_license_info_nth_license(1)
        licenses_page.should_be_download_license_button()
        licenses_page.should_be_revoke_button()

    def test_admin_can_download_license_file(self, browser):
        link = base_link + zzz_test_link
        licenses_page = LicencesPage(browser, link)
        licenses_page.open_license_info_nth_license(1)
        licenses_page.download_license_file()

    @pytest.mark.fff
    def test_admin_can_cancel_license_creation(self, browser):
        link = base_link + zzz_test_link
        licenses_page = LicencesPage(browser, link)
        licenses_page.open_add_new_license_page()
        licenses_page.cancel_adding_new_license()
        licenses_page.should_be_managing_licenses_page()
