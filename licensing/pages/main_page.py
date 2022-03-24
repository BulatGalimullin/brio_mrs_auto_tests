from .base_page import BasePage
from .locators import *
import time


class MainPage(BasePage):

    def should_be_main_page(self):
        assert self.browser.current_url == "https://licensing.briogroup.ru/", "This is not a main page"

    def is_access_denied(self):
        assert "Home/UnauthorizedUser" in self.browser.current_url, "This is not a page informing the user that access is denied"
        assert self.is_element_present(
            *MainPageLocators.RETURN_TO_MAIN_PAGE_LINK), "There is no return to home page link"

    def go_to_manage_users_page(self):
        self.browser.find_element(*MainPageLocators.MANAGE_USERS_LINK).click()



