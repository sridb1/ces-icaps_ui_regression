import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class CartPage:

    def __init__(self,driver):
        self.driver = driver

    remove_item = (By.XPATH,"//button[contains(@class,'tertiary cart-item-removal-button')]")
    checkout_btn = (By.XPATH, "//button[@data-ft='button-checkout']")
    undo_link = (By.XPATH, "//button[contains(@aria-label,'undo')]//span[contains(@class,'prefix-btn__inner')]")
    view_link = (By.XPATH, "//button[contains(@aria-label,'View')]//span[contains(@class,'prefix-btn__inner')]")
    save_favourites_btn = (By.XPATH, "//button[@data-ft='button-save-to-favourites']")
    confirm_alert = (By.XPATH, "//button[contains(@class,'prefix-btn--icon-tertiary-inverse')]")
    item_quantity = (By.XPATH, "//select[contains(@id, 'cart-item-quantity-select')]")

    def do_remove_item(self):
        return WebDriverWait(self.driver,30).until(EC.visibility_of_element_located(self.remove_item))

    def click_checkout_btn(self):
        return WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.checkout_btn))


    def do_save_favourites(self):
        return WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(self.save_favourites_btn))

    def click_view_link(self):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.view_link)))

    def close_confirm_alert(self):
        WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.confirm_alert))).click()

    def click_on_quantity(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.item_quantity)))

    def select_item_quantity(self,v_count):
        self.click_on_quantity().click()
        time.sleep(3)
        sel = Select(self.click_on_quantity())
        sel.select_by_visible_text(v_count)

    def click_checkout_btn(self):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.checkout_btn)).click()