from .base_page import BasePage
from .locators import DashboardPageLocators


class DashboardPage(BasePage):
    def fill_login_field(self):
        self.altdriver.find_object(*DashboardPageLocators.LOGIN_FIELD).click()

    def load(self):
        self.altdriver.load_scene('MainScene')

    def login(self, login, password, pin):
        self.altdriver.wait_for_object(*DashboardPageLocators.LOGIN_FIELD, timeout=5).set_text(login)
        self.altdriver.find_object(*DashboardPageLocators.PASSWORD_FIELD).set_text(password)
        self.altdriver.find_object(*DashboardPageLocators.PIN_FIELD).set_text(pin)
        self.altdriver.find_object(*DashboardPageLocators.PIN_CONFIRM_FIELD).set_text(pin)
        self.altdriver.find_object(*DashboardPageLocators.LOGIN_SIGNIN_BUTTON).click()
        assert self.altdriver.wait_for_object(*DashboardPageLocators.ADD_WIDGET_BUTTON, timeout=5)

    def is_displayed(self):
        """проверка что загружен дашбоард"""
        pass

    def is_user_signed_in(self):
        """проверка что пользователь авторизовался"""
        pass
