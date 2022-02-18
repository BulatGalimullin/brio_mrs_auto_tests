from .base_page import BasePage
from .locators import LoginPageLocators
import string
import random
import time


class LoginPage(BasePage):
    ##checks for login page
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        assert ("Login" or 'login') in self.browser.current_url, 'It is not a login page'
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented in the page"    #проверка, что есть форма логина
        assert True
    ##

    def login(self, username, password):
        self.browser.find_element(*LoginPageLocators.LOGIN_USERNAME).send_keys(username)
        self.browser.find_element(*LoginPageLocators.LOGIN_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    def should_be_error_message(self):
        assert self.is_element_present(*LoginPageLocators.ALERT_MESSAGE), "There is no alert message, probably correct inputs"


    def password_generator(self, length):

        length = int(length)
        # define data
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        num = string.digits
        symbols = string.punctuation

        # combine data
        all = lower + upper + num + symbols

        # use random
        temp = random.sample(all, length)

        # create password
        password = "".join(temp)
        return password


