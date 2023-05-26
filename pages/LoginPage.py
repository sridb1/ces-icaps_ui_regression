from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    email = (By.XPATH, "//input[@id='email']")
    password = (By.XPATH,"//input[@id='password']")
    submit = (By.XPATH, "//button[@type='submit']")
    check_point = (By.XPATH, "//button[contains(@class,'pp-skapa__btn pp-skapa__btn--secondary')]")
    # move later to appropriate page
    logout = (By.XPATH, "//button[normalize-space()='Log out']")
    # logout = (By.XPATH, "//button[contains(@class,'pp-skapa__btn pp-skapa__btn--secondary')]")
    forgot_pwd = (By.XPATH, "//a[normalize-space()='Forgot your password?']")

    def set_email(self,v_email):
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.email))).send_keys(v_email)

    def set_password(self,v_password):
        # return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.password)))
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.password))).send_keys(v_password)

    def click_forgot_pwd_link(self):
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.forgot_pwd))).click()

    def do_submit(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located(self.submit)))

    def do_click(self,by_locator):
        WebDriverWait(self.driver,30).until((EC.visibility_of_element_located(by_locator))).click()

    def validate_check_point(self):
        return WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.check_point)).is_displayed()