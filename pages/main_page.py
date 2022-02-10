from .base_page import BasePage
from .locators import *


class MainPage(BasePage):

    def go_to_register_page(self):
        link = self.browser.find_element(*BasePageLocators.REGISTER_LINK)
        link.click()

    def add_new_user(self, email="test@test", password="Passw0rd"):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_NAME).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SURNAME).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PATRONYMIC).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_ORGANIZATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_CONFIRM).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFID_CHECKBOX).click()
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
