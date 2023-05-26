import inspect
import logging
import os
import string
import random

import pytest
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ProfilePage import ProfilePage

""" This class contains all methods and utilities useful in test case scripts"""


@pytest.mark.usefixtures("setup")
class BaseClass:

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler(os.getcwd()+'\\reports\\logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger

    def login(self,getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        login=LoginPage(self.driver)
        self.driver.get(str(getData["url"]) + "/profile/login")
        self.login_ingka_profile(getData)
        home_page.accept_cookies().click()
        self.clear_popup()
        # login.set_email(getData["loginuser"])
        login.set_email(self.v_email)
        login.set_password(getData["loginpwd"])
        login.do_submit().click()
        assert True == login.validate_check_point()
        log.info("Profile Login is Successfull")

    def generate_random_string(length: int) -> str:
        # Use the ascii_letters and digits constants from the string module to create a string of all valid characters
        all_characters = string.ascii_letters + string.digits
        # Use the sample function from the random module to select `length` random characters from the all_characters string
        return ''.join(random.sample(all_characters, length))

    def verifyLinkPresence(self, text):
        element = WebDriverWait(self.driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, text)))

    def clickButton(self,text):
        button = self.driver.find_element_by_xpath(text)
        self.driver.execute_script("arguments[0].click();", button)

    def selectOptionByText(self,locator,text):
        sel = Select(locator)
        sel.select_by_visible_text(text)

    #     yet to use of below method
    def do_click(self,by_locator):
        WebDriverWait(self.driver,10).until((EC.visibility_of_element_located(by_locator))).click()

    #     yet to use of below method
    def do_send_keys(self,by_locator,text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self,by_locator):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """yet to use below method"""

    def get_text_value(self, locator):
        text1 = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator)).text
        return text1

    def get_title(self,title):
        element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(title))

    def validate_url_check_point(self,text_in_url):
        return WebDriverWait(self.driver,20).until(EC.url_contains(text_in_url))

    def press_home_key(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.HOME)
        actions.perform()

    def logout(self,getData):
        log = self.getLogger()
        login = LoginPage(self.driver)
        self.driver.get(str(getData["url"]) + "/profile/login")
        login.do_click(login.logout)

    def login_ingka_profile(self, getData):
        wait = WebDriverWait(self.driver, 5)

        try:
            # Wait for the username field to be clickable with a timeout of 5 seconds
            username_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='username']")), 5)

            # Input the username if the field is present
            if username_field:
                username_field.clear()
                username_field.send_keys(getData["ikeauser"])

                # Find the submit button and click it
                submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@name='action']")))
                submit_button.click()

                # Wait for the password field to be clickable with a timeout of 5 seconds
                password_field = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='passwd']")), 5)

                # Input the password if the field is present
                if password_field:
                    password_field.clear()
                    password_field.send_keys(getData["ikeapwd"])

                    # Find the login button and click it
                    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']")))
                    login_button.click()

        except:
            # If any of the above steps fails, do nothing
            pass

    def clear_popup(self):
        close_button_locator = (By.XPATH, "//span[contains(@class,'close-btn icon-cross_thin_64')]")
        close_button = None
        try:
            close_button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(close_button_locator))
        except TimeoutException:
            # no pop-up window found, continue with the test
            pass
        if close_button is not None:
            close_button.click()

