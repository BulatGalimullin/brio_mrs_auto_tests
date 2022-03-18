from .pages.login_page import LoginPage
import pytest
import time


link = "https://identity.briogroup.ru/Account/Login"


class TestLoginPage:
    @pytest.mark.parametrize('login,password',
                         [(" ", "no_login"), ("no_password", "  "), ("  ", "  "), ("incorrect", "incorrect")])
    def test_try_to_login_with_incorrect_inputs(self, browser, login, password):
        login_page = LoginPage(browser, link)
        login_page.open()
        login_page.login(login, password)
        time.sleep(0.01)
        login_page.should_be_error_message()


# @pytest.mark.need_review
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
#                                                "/?promo=offer7", marks=pytest.mark.xfail),
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     page = ProductPage(browser, link)  # инициализируем page object,
#     page.open()  # open the page with product
#     page.add_to_card()  # click to add to the basket button
#     page.solve_quiz_and_get_code()  # solve quiz
#     page.is_item_added_to_card()  # check that the product indeed added to the basket
#
#
# # negative tests for presence of success message after adding to the card
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)  # инициализируем page object,
#     page.open()  # open the page with product
#     page.add_to_card()  # click to add to the basket button
#     page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)  # инициализируем page object,
#     page.open()  # open the page with product
#     page.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
#     page = ProductPage(browser, link)  # инициализируем page object,
#     page.open()  # open the page with product
#     page.add_to_card()  # click to add to the basket button
#     page.should_success_message_disappeared()
#
#
# # go to the product page
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#
#
# @pytest.mark.need_review
# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()
#     page.go_to_login_page()
#     login_page = LoginPage(browser, browser.current_url)  # инициализация страницы логина
#     login_page.should_be_login_page()
#
#
# @pytest.mark.need_review
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser, browser.current_url)
#     basket_page.should_be_empty_basket()
#     basket_page.should_be_empty_basket_message()










