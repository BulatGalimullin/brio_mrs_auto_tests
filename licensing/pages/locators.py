from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "a[href$=Login]")
    LOGOUT_LINK = (By.CSS_SELECTOR, "a[href$=Logout]")


class MainPageLocators:
    RETURN_TO_MAIN_PAGE_LINK = (By.CSS_SELECTOR, "main a.nav-link[href='/']")
    MANAGE_USERS_LINK = (By.CSS_SELECTOR, "a[href='/Users']")


class UsersPageLocators:
    USERS_TABLE = (By.CSS_SELECTOR, "table.table.table-striped")
    USERS_TABLE_FIRST_LOGIN = (By.CSS_SELECTOR, 'table > tbody > tr:first-child  > td:nth-child(2) > a')
    # USERS_TABLE_SURNAME = (By.XPATH, '//table[@class="table table-striped"]//th[text()="Surname"]')
    # USERS_TABLE_NAME = (By.XPATH, '//table[@class="table table-striped"]//th[text()="Name"]')
    # USERS_TABLE_PATRONYMIC = (By.XPATH, '//table[@class="table table-striped"]//th[text()="Patronymic"]')
    # USERS_TABLE_EMAIL = (By.XPATH, '//table[@class="table table-striped"]//th[text()="Email"]')

    FIRST_PAGE = (By.CSS_SELECTOR, "ul.pagination > li:first-child > a")
    LAST_PAGE = (By.CSS_SELECTOR, "ul.pagination > li:last-child > a")
    PENULTIMATE_PAGE = (By.CSS_SELECTOR, "ul.pagination > li:nth-last-child(2) > a")

    #
    PAGE_NUMBER = []
    for n in range(20):
        PAGE_NUMBER.append((By.CSS_SELECTOR, F"ul.pagination > li:nth-child({n + 1}) > a"))
    #

    SEARCH_PLACE = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[type=submit]")
    #
    DELETE_BUTTON_USER_NUMBER = []
    for n in range(10):
        user_to_delete = (By.CSS_SELECTOR, F"tr:nth-child({n}) td:last-child > a.btn-danger")
        DELETE_BUTTON_USER_NUMBER.append(user_to_delete)
    #
    USERS_TABLE_FIRST_LOGIN_FIELD = (By.CSS_SELECTOR, "tr:nth-child(1) td:nth-child(2)")
    DELETE_CONFIRMATION_BUTTON = (By.CSS_SELECTOR, "button.btn-danger")

    ADD_USER_BUTTON = (By.CSS_SELECTOR, "div.add-item-form > a")
    ADD_USER_LOGIN_FIELD = (By.ID, "Login")
    ADD_USER_FIRSTNAME_FIELD = (By.ID, "FirstName")
    ADD_USER_FAMILYNAME_FIELD = (By.ID, "FamilyName")
    ADD_USER_PATRONYMICNAME_FIELD = (By.ID, "PatronymicName")
    ADD_USER_EMAIL_FIELD = (By.ID, "Email")
    ADD_USER_PASSWORD_FIELD = (By.ID, "Password")
    ADD_USER_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ADD_USER_CANCEL_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-secondary.mt-3")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "div.form-group~button[value=login]") # ?????????????? ????????????????
    LOGIN_USERNAME = (By.CSS_SELECTOR, "input#Username")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input#Password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[value = 'login']")
    REMEMBER_ME_CHECKBOX = (By.ID, "RememberLogin")
    ALERT_MESSAGE = (By.CSS_SELECTOR, "div.alert-danger")
    CANCEL_BUTTON = (By.CSS_SELECTOR, "button[value = 'cancel']")
    POST_LOGOUT_REDIRECT_LINK = (By.CLASS_NAME, "PostLogoutRedirectUri")


class LicensesPageLocators:
    """Licenses table"""
    LICENSES_TABLE = (By.CSS_SELECTOR, "table.table.table-striped")
    ADD_LICENSE_BUTTON = (By.CSS_SELECTOR, ".add-item-form > a.btn")
    CREATION_DATE_FIRST_LICENSE = (By.CSS_SELECTOR, "tr:nth-child(1) > td:nth-child(3)")

    OPEN_LICENSE_NUMBER = []
    for n in range(10):
        open_license_button = (By.CSS_SELECTOR, F"tr:nth-child({n}) td:last-child > a.btn-primary")
        OPEN_LICENSE_NUMBER.append(open_license_button)

    FIRST_PAGE = (By.CSS_SELECTOR, "ul.pagination > li:first-child > a")
    LAST_PAGE = (By.CSS_SELECTOR, "ul.pagination > li:last-child > a")
    LICENSES_PENULTIMATE_PAGE = (By.CSS_SELECTOR, "ul.pagination > li:nth-last-child(2) > a")

    PAGE_NUMBER = []
    for n in range(20):
        PAGE_NUMBER.append((By.CSS_SELECTOR, F"ul.pagination > li:nth-child({n + 1}) > a"))

    """Licenses info"""
    DOWNLOAD_LICENSE_BUTTON = (By.CSS_SELECTOR, "div.d-flex > a")
    REVOKE_BUTTON = (By.CSS_SELECTOR, "div.d-flex > form")
    SUBMIT_ADD_LICENSE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    CANCEL_ADD_LICENSE_BUTTON = (By.CSS_SELECTOR, "a.btn-secondary.mt-3")
    TIME_LIMIT_FROM_LAUNCH_CHECKBOX = (By.CSS_SELECTOR, '[data-target="#timeLimitFromLaunchEdit"]')
    TIME_LIMIT_FROM_LAUNCH_INPUT_FIELD = (By.ID, 'fromLaunchTime')
    TIME_LIMIT_CUMULATIVE_CHECKBOX = (By.CSS_SELECTOR, '[data-target="#timeLimitCumulativeEdit"]')
    TIME_LIMIT_CUMULATIVE_INPUT_FIELD = (By.ID, 'cumulativeTime')
    TIME_LIMIT_FROM_FIRST_USE_CHECKBOX = (By.CSS_SELECTOR, '[data-target="#timeLimitFromFirstUseEdit"]')
    TIME_LIMIT_FROM_FIRST_USE_DAYS_FIELD = (By.ID, 'TimeLimits_FromFirstUse__TimeDays')
    TIME_LIMIT_FROM_FIRST_USE_HOURS_FIELD = (By.ID, 'TimeLimits_FromFirstUse__TimeHours')
    TIME_LIMIT_FROM_FIRST_USE_MINUTES_FIELD = (By.ID, 'TimeLimits_FromFirstUse__TimeMinutes')
