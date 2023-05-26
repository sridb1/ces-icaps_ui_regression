import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class ProfilePage:

    def __init__(self,driver):
        self.driver = driver

    """Web elements present in the profile page"""

    # profile_details = (By.XPATH, "//a[@data-testid='nav-profile-details']")
    profile_details = (By.XPATH, "//span[normalize-space()='View and edit your profile details']")
    edit_personal_info = (By.XPATH,"//button[contains(@class,'skapaWrapperPrefixNoOutline') or contains(@class,'skapa__btn--secondary')]")
    # edit_personal_info = (By.XPATH,"//button[contains(@class,'secondary skapaWrapperPrefixNoOutline')]")
    first_name = (By.CSS_SELECTOR,"#first-name")
    last_name = (By.CSS_SELECTOR,"#last-name")
    region_list = (By.XPATH,"//select[@id='Region']")
    city_list = (By.XPATH,"//select[@id='City']")
    barangay_list = (By.XPATH,"//select[@id='Barangay']")
    address_line1 = (By.CSS_SELECTOR,"#address-line-1")
    city = (By.CSS_SELECTOR,"#city")
    postal_code = (By.CSS_SELECTOR,"#postal-code")
    phone = (By.CSS_SELECTOR,"#phone")
    inline_msg = (By.XPATH,"//p[contains(@class,'inline-message')]")
    preferred_store = (By.XPATH, "//a[@data-testid='nav-preferred-store']")
    # change_password = (By.XPATH,"//a[@data-testid='nav-change-password']")
    change_password = (By.XPATH,"//span[normalize-space()='Change password']")
    # delete_account = (By.XPATH, "//a[@data-testid='nav-delete-account']")
    delete_account = (By.XPATH, "//button[@data-testid='nav-delete-account']")
    current_password = (By.XPATH,"//input[@id='current-password']")
    new_password = (By.XPATH,"//input[@id='new-password']")
    confirm_password = (By.XPATH,"//input[@id='new-confirmed-password']")
    email = (By.XPATH, "//input[@id='email']")
    password = (By.XPATH,"//input[@id='password']")
    submit = (By.XPATH, "//button[@type='submit']")
    save_btn = (By.XPATH, "//button[@class='pp-skapa__btn pp-skapa__btn--primary pp-skapa__btn--fluid']")
    add_address_btn = (By.XPATH,"//button[@id='buttonId']")
    logout = (By.XPATH, "//button[normalize-space()='Log out']")
    # logout = (By.XPATH, "//button[contains(@class,'pp-skapa__btn pp-skapa__btn--secondary')]")


    def view_profile_details(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.profile_details)))

    def do_change_password(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located(self.change_password)))

    def change_preferred_store(self):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.preferred_store)))

    def do_delete_account(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.delete_account)))

    def set_password(self,v_password):
        WebDriverWait(self.driver, 15).until((EC.visibility_of_element_located(self.password))).send_keys(v_password)

    def set_current_password(self,v_password):
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.current_password))).send_keys(v_password)

    def set_new_password(self,v_password):
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.new_password))).send_keys(v_password)

    def set_confirm_password(self,v_password):
        WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.confirm_password))).send_keys(v_password)

    def do_submit(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.submit)))

    def do_edit_personal_info(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located(self.edit_personal_info)))

    def edit_first_name(self,text):
        first_name_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.first_name))
        first_name_field.send_keys(Keys.CONTROL,'a')
        first_name_field.send_keys(Keys.BACK_SPACE)
        first_name_field.send_keys(text)
        # WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.first_name))).send_keys(Keys.BACK_SPACE)
        # WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.first_name))).send_keys(text)

    def edit_last_name(self,text):
        last_name_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.last_name))
        last_name_field.send_keys(Keys.CONTROL, 'a')
        last_name_field.send_keys(Keys.BACK_SPACE)
        last_name_field.send_keys(text)
        # WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.last_name))).send_keys(Keys.CONTROL,'a')
        # WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.last_name))).send_keys(Keys.BACK_SPACE)
        # WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.last_name))).send_keys(text)

    def edit_phone(self,text):
        phone_field = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.phone))
        phone_field.send_keys(Keys.CONTROL, 'a')
        phone_field.send_keys(Keys.BACK_SPACE)
        phone_field.send_keys(text)
        # WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.phone))).send_keys(Keys.CONTROL,'a')
        # WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.phone))).send_keys(Keys.BACK_SPACE)
        # WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.phone))).send_keys(text)

    def do_save(self):
        WebDriverWait(self.driver,30).until((EC.visibility_of_element_located(self.save_btn))).click()

    def click_add_address_btn(self):
        WebDriverWait(self.driver,10).until((EC.visibility_of_element_located(self.add_address_btn))).click()

    def validate_check_point(self):
        return WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.inline_msg)).is_displayed()

    def add_address_line1(self,text):
        WebDriverWait(self.driver,10).until((EC.visibility_of_element_located(self.address_line1))).send_keys(text)

    def add_city(self,text):
        WebDriverWait(self.driver,30).until((EC.visibility_of_element_located(self.city))).send_keys(text)

    def add_postal_code(self,text):
        WebDriverWait(self.driver,10).until((EC.visibility_of_element_located(self.postal_code))).send_keys(text)

    def click_on_region(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.region_list)))

    def select_region(self):
        time.sleep(2)
        sel = Select(self.click_on_region())
        sel.select_by_index(1)

    def select_city(self):
        WebDriverWait(self.driver,30).until((EC.visibility_of_element_located(self.city_list))).click()
        sel = Select(WebDriverWait(self.driver,30).until((EC.element_to_be_clickable(self.city_list))))
        sel.select_by_index(1)

    def select_barangay(self):
        sel = Select(WebDriverWait(self.driver,30).until((EC.element_to_be_clickable(self.barangay_list))))
        sel.select_by_index(1)
