from altunityrunner import By


class DashboardPageLocators:
    LOGIN_POPUP = (By.NAME, "Popup - Local SignIn(Clone)")
    LOGIN_FIELD = (By.NAME, "InputField - Login")
    PASSWORD_FIELD = (By.NAME, "InputField - Password")
    PIN_FIELD = (By.NAME, "InputField - PIN")
    PIN_CONFIRM_FIELD = (By.NAME, "InputField - PIN Confirmation")
    LOGIN_SIGNIN_BUTTON = (
    By.NAME, "PopupCanvas/Popup - Local SignIn(Clone)/Container/Button Container/UIButton - Sign In")
    LOGIN_CANCEL_BUTTON = (
    By.NAME, "PopupCanvas/Popup - Local SignIn(Clone)/Container/Button Container/UIButton - Cancel")
    ADD_WIDGET_BUTTON = (By.NAME, "Scroll View - Widgets/Viewport/Content/Add widget")
