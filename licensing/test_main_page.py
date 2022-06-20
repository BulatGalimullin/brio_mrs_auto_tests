from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.users_page import UsersPage
import pytest

link = "https://licensing.briogroup.ru"


class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open() # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина
        login_page = LoginPage(browser, browser.current_url) # инициализация страницы логина
        login_page.should_be_login_page() # проверка, что это действительно страница логина

    def test_login_with_correct_inputs(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login('test', 'Qwe123!')
        page.should_be_authorized_user()

    def test_cancel_button_in_login_page_should_return_not_authorized_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.cancel_login()
        login_page.should_not_be_authorized_user()
        page.is_access_denied()


class TestUserActionsNoRemember:

    @pytest.fixture(scope='function', autouse=True)
    def setup_method(self, browser):
        self.link = "https://licensing.briogroup.ru"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.login('test', 'Qwe123!')
        self.login_page.should_be_authorized_user()

    def test_logout(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.logout()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_identity_server_page()
        login_page.return_to_home_from_identity_server_page()
        login_page.should_not_be_authorized_user()


class TestAdminActions:
    @pytest.fixture(scope='function', autouse=True)
    def setup_method(self, browser):
        self.link = "https://licensing.briogroup.ru"
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.login('admin', 'Qwe123!')
        self.login_page.should_be_authorized_user()

    def test_admin_open_list_of_users(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_manage_users_page()
        users_page = UsersPage(browser, browser.current_url)
        users_page.should_be_manage_users_page()



















