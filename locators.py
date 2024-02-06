from selenium.webdriver.common.by import By

class TestLocators:
    LOGIN_TO_ACCOUNT_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_large__G21Vg']"
    INPUTS_FOR_LOGIN = By.XPATH, "//input[@class='text input__textfield text_type_main-default']"
    LOGIN_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    PROFILE_BUTTON = By.LINK_TEXT, 'Профиль'
    LOGOUT_BUTTON = By.XPATH, "//button[@class='Account_button__14Yp3 text text_type_main-medium text_color_inactive']"
    PERSONAL_ACCOUNT_BUTTON = By.LINK_TEXT, 'Личный Кабинет'
    CONSTRUCTOR_BUTTON = By.LINK_TEXT, 'Конструктор'
    STELLAR_BURGERS_LOGO = By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']"
    REGISTRATION_LINK = By.LINK_TEXT, 'Зарегистрироваться'
    PASSWORD_RECOVERY_LINK = By.LINK_TEXT, 'Восстановить пароль'
    LOGIN_LINK = By.LINK_TEXT, 'Войти'
    CONSTRUCTOR_TABS = By.XPATH, "//span[@class='text text_type_main-default']"
    CONSTRUCTOR_SELECTED_TAB = By.XPATH, "//div[@class='tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']"
    REGISTRATION_BUTTON = By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa']"
    INCORRECT_PASSWORD_ERROR = By.XPATH, "//p[@class='input__error text_type_main-default']"


