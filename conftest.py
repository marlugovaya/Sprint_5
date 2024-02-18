import pytest
from selenium import webdriver
from Sprint_5.locators import TestLocators
from Sprint_5.data import TestData
import time


@pytest.fixture(scope='function')
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    #chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON).click()
    driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(TestData.GOOD_LOGIN_PASSWORD[0])
    driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(TestData.GOOD_LOGIN_PASSWORD[1])
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
    yield driver
