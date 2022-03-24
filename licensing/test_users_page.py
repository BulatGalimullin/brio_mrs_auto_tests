from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.users_page import UsersPage
import pytest
import random
import time

base_link = "https://licensing.briogroup.ru"
link = base_link + '/Users'


class TestAdminActions:

    @pytest.fixture(scope='function', autouse=True)
    def setup_method(self, browser):
        self.link = base_link
        self.page = MainPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)
        self.login_page.login('admin', 'Qwe123!')
        self.login_page.should_be_authorized_user()

    def test_change_users_page_with_last_button(self, browser):
        page = UsersPage(browser, link)
        page.open()
        page.go_to_the_page_number('last')
        page.should_be_manage_users_page()

    def test_change_users_page_with_first_button(self, browser):
        page = UsersPage(browser, link)
        page.open()
        page.go_to_the_page_number('first')
        page.should_be_manage_users_page()

    @pytest.mark.test1
    def test_change_users_page_with_numbers_button(self, browser):
        page = UsersPage(browser, link)
        page.open()
        page.go_to_the_page_number(2)
        time.sleep(5)
        page.should_be_manage_users_page()

    def test_use_users_search(self, browser):
        page = UsersPage(browser, link)
        page.open()
        page.search_user("zzz_test")
        page.is_this_user_presented_in_the_users_page("zzz_test")
    # TODO: всего лишь 1 тест на поиск? Серьёзно?

    @pytest.mark.test
    def test_admin_can_go_to_add_users(self, browser):
        page = UsersPage(browser, link)
        page.open()
        page.go_to_add_users_page()
        page.should_be_add_users_page()

    def test_add_users_page_email_field_checks(self, browser):
        link = self.link + '/Users/AddUser'
        page = UsersPage(browser, link)
        page.open()
        page.fill_user_email_field(F"test@test{random.randrange(10000000)}")
    # TODO: недописан

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
        self.page = UsersPage(browser, browser.current_url)
        self.page.delete_user(self.login)
        #TODO: удалять пользователя таким способом - не очень хороший, переделать

    def test_admin_can_add_user_with_patronymic(self, browser):
        link = self.link + '/Users/AddUser'
        page = UsersPage(browser, link)
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
        page = UsersPage(browser, link)
        page.open()
        page.fill_user_login_field(self.login)
        page.fill_user_first_name_field("test")
        page.fill_user_family_name_field("test")
        page.fill_user_email_field(F"test@test{random.randrange(10000000)}")
        page.fill_user_password_field("Qwe1234!")
        page.submit_user_adding()
        page.is_this_user_presented_in_the_users_page(self.login)

