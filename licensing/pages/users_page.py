from .base_page import BasePage
from .locators import *
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UsersPage(BasePage):

    # ACTIONS

    def go_to_the_page_number(self, number):
        if isinstance(number, str) and number.casefold() == 'first':
            self.browser.find_element(*UsersPageLocators.FIRST_PAGE).click()
            assert 'page=1' in self.browser.current_url, "This is not first page"
        elif isinstance(number, str) and number.casefold() == 'last':
            self.browser.find_element(*UsersPageLocators.LAST_PAGE).click()
            self.should_be_the_last_page()
        elif isinstance(number, int) and number <= 20:
            current_page = self.browser.find_element(*UsersPageLocators.PAGE_NUMBER[number])
            current_page.click()
        assert F'page={number}' in self.browser.current_url, F"This is not page number {number}"

    def search_user(self, user):
        self.browser.find_element(*UsersPageLocators.SEARCH_PLACE).send_keys(user)
        self.browser.find_element(*UsersPageLocators.SEARCH_BUTTON).click()

    def go_to_add_users_page(self):
        self.browser.find_element(*UsersPageLocators.ADD_USER_BUTTON).click()

    def open_first_login_in_the_users_table(self):
        self.browser.find_element(*UsersPageLocators.USERS_TABLE_FIRST_LOGIN_FIELD).click()


    def add_new_user(self, email="test@test", password="Passw0rd"):
        self.fill_user_login_field(login)
        self.fill_user_first_name_field(firstname)
        self.fill_user_family_name_field(familyname)
        self.fill_user_email_field(email)
        self.fill_user_password_field(password)

    def fill_user_login_field(self, login):
        self.browser.find_element(*UsersPageLocators.ADD_USER_LOGIN_FIELD).send_keys(login)

    def fill_user_first_name_field(self, firstname):
        self.browser.find_element(*UsersPageLocators.ADD_USER_FIRSTNAME_FIELD).send_keys(firstname)

    def fill_user_family_name_field(self, familyname):
        self.browser.find_element(*UsersPageLocators.ADD_USER_FAMILYNAME_FIELD).send_keys(familyname)

    def fill_user_patronymic_field(self, patronymic):
        self.browser.find_element(*UsersPageLocators.ADD_USER_PATRONYMICNAME_FIELD).send_keys(patronymic)

    def fill_user_email_field(self, email):
        self.browser.find_element(*UsersPageLocators.ADD_USER_EMAIL_FIELD).send_keys(email)

    def fill_user_password_field(self, password):
        self.browser.find_element(*UsersPageLocators.ADD_USER_PASSWORD_FIELD).send_keys(password)

    def submit_user_adding(self):
        self.browser.find_element(*UsersPageLocators.ADD_USER_SUBMIT_BUTTON).click()

    def cancel_user_adding(self):
        self.browser.find_element(*UsersPageLocators.ADD_USER_CANCEL_BUTTON).click()

    def delete_user(self, user):
        self.search_user(user)
        if self.browser.find_element(*UsersPageLocators.USERS_TABLE_FIRST_LOGIN_FIELD).text == user:
            self.browser.find_element(*UsersPageLocators.DELETE_BUTTON_USER_NUMBER[1]).click()
        else:
            assert False, F"Didn't find user {user} in the list"
        if self.browser.find_element(*UsersPageLocators.ADD_USER_LOGIN_FIELD).text == user:
            time.sleep(5)
            self.browser.find_element(*UsersPageLocators.DELETE_CONFIRMATION_BUTTON).click()
            time.sleep(5)
        else:
            assert False, F"Couldn't delete user {user}"

    # CHECKS

    def should_be_add_users_page(self):
        assert self.is_element_present(*UsersPageLocators.ADD_USER_LOGIN_FIELD), "There is no login field"
        assert self.is_element_present(*UsersPageLocators.ADD_USER_FIRSTNAME_FIELD), "There is no first name field"
        assert self.is_element_present(*UsersPageLocators.ADD_USER_FAMILYNAME_FIELD), "There is no family name field"
        assert self.is_element_present(
            *UsersPageLocators.ADD_USER_PATRONYMICNAME_FIELD), "There is no patronymic name field"
        assert self.is_element_present(*UsersPageLocators.ADD_USER_EMAIL_FIELD), "There is no email field"
        assert self.is_element_present(*UsersPageLocators.ADD_USER_PASSWORD_FIELD), "There is no password field"

    def should_be_manage_users_page(self):
        assert "/Users" in self.browser.current_url, "Url of the page doesn't contain '/Users'"
        assert self.is_element_present(*UsersPageLocators.USERS_TABLE), "There is no table with registered users"

    def should_be_the_last_page(self):
        assert self.browser.find_element(*UsersPageLocators.PENULTIMATE_PAGE).get_attribute(
            "href") in self.browser.current_url, "This is not the last page"

    def is_this_user_presented_in_the_users_page(self, user):
        users_table = self.browser.find_element(*UsersPageLocators.USERS_TABLE).text
        assert user in users_table, F"There is no requested user in following table: {users_table}"