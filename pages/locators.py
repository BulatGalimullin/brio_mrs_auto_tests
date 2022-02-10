from selenium.webdriver.common.by import By

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href$=Login]")



class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "div.form-group~button[value=login]") # спорный селектор
    LOGIN_USERNAME = (By.CSS_SELECTOR, "input#Username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value = 'login']")
    REGISTRATION_SURNAME = (By.ID, "input-37")
    REGISTRATION_PATRONYMIC = (By.ID, "input-40")
    REGISTRATION_ORGANIZATION = (By.ID, "input-43")
    REGISTRATION_EMAIL = (By.ID, "input-46")
    REGISTRATION_PASSWORD = (By.ID, "input-49")
    REGISTRATION_PASSWORD_CONFIRM = (By.ID, "input-52")
    REGISTRATION_CONFID_CHECKBOX = (By.CSS_SELECTOR, "div.v-input--selection-controls__ripple")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button.mx-auto.mr-2")

