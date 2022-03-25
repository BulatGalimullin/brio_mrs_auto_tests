from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.licensing_page import LicencesPage
import pytest


base_link = "https://licensing.briogroup.ru"


class TestLicencesPagesAsAdmin:

    @pytest.fixture(scope='function', autouse=True)
    def setup_method(self, browser):
        self.link = base_link
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.login('admin', 'Qwe123!')
        self.login_page.should_be_authorized_user()

    def test_change_licenses_page_with_first_button(self, browser):
        link = base_link + '/Licenses?userId=97de743a-8a8a-4524-bef9-2fdc12f144de'
        page = LicencesPage(browser, link)
        page.open()
        page.go_to_the_page_number('first')
        page.should_be_manage_users_page()

        def test_change_users_page_with_numbers_button(self, browser):
            page = UsersPage(browser, link)
            page.open()
            page.go_to_the_page_number(2)
            page.should_be_manage_users_page()
