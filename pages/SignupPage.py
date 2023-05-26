from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupPage:

    def __init__(self,driver):
        self.driver = driver

    # web elements in the signup page
    firstname = (By.ID, 'first-name')
    lastname = (By.ID, 'last-name')
    email = (By.ID, 'email')
    password = (By.ID, 'password')
    privacy_checkbox = (By.ID, 'privacy-policy-checkbox')
    submit = (By.XPATH, "//button[@type='submit']")
    logout = (By.XPATH, "//button[normalize-space()='Log out']")

    def set_firstname(self,v_firstname):
        # wait= self.driver.find_element(*LoginPage.cookieAccept)
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.firstname))).send_keys(v_firstname)

    def set_lastname(self,v_lastname):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.lastname))).send_keys(v_lastname)

    def set_email(self,v_email):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.email))).send_keys(v_email)

    def set_password(self, v_password):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.password))).send_keys(v_password)

    def select_privacy_checkbox(self):
        self.driver.find_element(*self.privacy_checkbox).send_keys(Keys.SPACE)

    def do_submit(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located(self.submit)))

    def validate_check_point(self):
        return WebDriverWait(self.driver,25).until(EC.visibility_of_element_located(self.logout)).is_displayed()