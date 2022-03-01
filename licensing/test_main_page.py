from .pages.main_page import MainPage
from .pages.login_page import LoginPage
import pytest
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

    @pytest.mark.test
    def test_login_with_correct_inputs(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login('test', 'Qwe123!')
        page.should_be_authorized_user()

    @pytest.mark.test
    def test_cancel_button_in_login_page_should_return_previous_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.cancel_login()
        login_page.should_not_be_authorized_user()
        time.sleep(5)
        page.should_be_main_page()


















class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        self.page = ProductPage(browser, self.link)
        self.page.open()
        self.page.go_to_login_page()
        self.login_page = LoginPage(browser, browser.current_url)

        f = faker.Faker() # faker object
        email = f.email()  # fake email generation
        password = self.login_page.password_generator(9) # password generation

        self.login_page.register_new_user(email, password)
        self.login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = MainPage(browser, self.link)  # инициализируем page object,
        page.open()  # open the page with product
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, self.link)  # инициализируем page object,
        page.open()  # open the page with product
        page.add_to_card()  # click to add to the basket button
        page.is_item_added_to_card()  # check that the product indeed added to the basket

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
    basket_page.should_be_empty_basket_message()




