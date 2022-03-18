from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
import random
import time

link = "https://licensing.briogroup.ru"


@pytest.mark.login_guest
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

    def test_open_list_of_users(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.manage_users()
        page.should_be_manage_users_page()

    def test_change_users_page_with_last_button(self, browser):
        link = self.link + '/Users'
        page = MainPage(browser, link)
        page.open()
        page.go_to_the_page_number('last')
        page.should_be_manage_users_page()

    def test_change_users_page_with_first_button(self, browser):
        link = self.link + '/Users'
        page = MainPage(browser, link)
        page.open()
        page.go_to_the_page_number('first')
        page.should_be_manage_users_page()

    def test_change_users_page_with_numbers_button(self, browser):
        link = self.link + '/Users'
        page = MainPage(browser, link)
        page.open()
        page.go_to_the_page_number(1)
        page.should_be_manage_users_page()

    def test_use_users_search(self, browser):
        link = self.link + '/Users'
        page = MainPage(browser, link)
        page.open()
        page.search_user("zzz_test")
        page.is_this_user_presented_in_the_users_page("zzz_test")
    # TODO: всего лишь 1 тест на поиск? Серьёзно?

    def test_admin_can_go_to_add_users(self, browser):
        link = self.link + '/Users/AddUser'
        page = MainPage(browser, link)
        page.open()
        page.go_to_add_users_page()
        page.should_be_add_users_page()

    def test_add_users_page_email_field_checks(self, browser):
        link = self.link + '/Users'
        page = MainPage(browser, link)
        page.open()
        page.fill_user_email_field(F"test@test{random.randrange(10000000)}")


@pytest.mark.test
class TestAdminAddUsers:
    @pytest.fixture(scope='function', autouse=True)
    def setup_method(self, browser):
        self.link = "https://licensing.briogroup.ru"
        self.login = "000test" + str(random.randrange(100000))
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.login('admin', 'Qwe123!')
        self.login_page.should_be_authorized_user()
        yield
        self.page.delete_user(self.login)
        #TODO: удалять пользователя таким способом - не очень хороший, переделать

    def test_admin_can_add_user_with_patronymic(self, browser):
        link = self.link + '/Users/AddUser'
        page = MainPage(browser, link)
        page.open()
        page.fill_user_login_field(self.login)
        page.fill_user_first_name_field("test")
        page.fill_user_family_name_field("test")
        page.fill_user_patronymic_field("test")
        page.fill_user_email_field(F"test@test{random.randrange(10000000)}")
        page.fill_user_password_field("Qwe1234!")
        page.submit_user_adding()
        page.is_this_user_presented_in_the_users_page(self.login)

    def test_admin_can_add_user_without_patronymic(self, browser):
        link = self.link + '/Users/AddUser'
        page = MainPage(browser, link)
        page.open()
        page.fill_user_login_field(self.login)
        page.fill_user_first_name_field("test")
        page.fill_user_family_name_field("test")
        page.fill_user_email_field(F"test@test{random.randrange(10000000)}")
        page.fill_user_password_field("Qwe1234!")
        page.submit_user_adding()
        page.is_this_user_presented_in_the_users_page(self.login)



















