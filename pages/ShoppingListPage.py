import time

from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class ShoppingListPage:

    def __init__(self,driver):
        self.driver = driver

    new_list = (By.XPATH,"//button[contains(@class,'prefix-btn--primary')]/child::span[contains(@class,'prefix-btn__inner')]")
    list_name = (By.XPATH, "//input[contains(@id,'create-list') or contains(@id,'new-list-field')]")
    rename_list = (By.ID, 'rename-field')
    save_list = (By.XPATH, "//span[@class='skapa-wrapper-prefix-btn__label'][normalize-space()='Save']")
    confirm_alert = (By.XPATH, "//button[contains(@class,'prefix-btn--icon-tertiary-inverse')]")
    # list_actions_button = (By.XPATH, "//section[@class='ListActions_listActions__7FurV']/child::button[2]")
    list_actions_button = (By.XPATH, "//button[@data-testid='list-actions-more-button']//span[@class='skapa-wrapper-prefix-btn__inner']")
    move_items_link = (By.XPATH, "//li[contains(@id,'actionlist-0')]/child::button[contains(@class,'item__action')]")
    new_list2 = (By.XPATH, "//button[contains(@class,'--secondary skapa-wrapper-prefix-btn--fluid')]")
    vmove_items_new_list = (By.XPATH, "//button[contains(@class,'skapa-wrapper-prefix-choice-item__action')]")
    view_link = (By.XPATH, "//span[contains(@class,'skapa-wrapper-prefix-choice-item__title')]")
    back_to_lists = (By.XPATH, "//button[contains(@class,'backButton')]")
    list1_name_link = (By.XPATH, "//*[text()='" + 'ShoppingList1' + "']")
    list2_name_link = (By.XPATH, "//*[text()='" + 'ShoppingList2' + "']")
    list_options = (By.XPATH,"//button[contains(@class,'prefix-btn--icon-tertiary')]")
    remove_list_link = (By.XPATH, "//span[contains(text(),'Remove list')]")
    change_list_link = (By.XPATH, "//span[contains(text(),'Change name of list')]")
    remove_button = (By.XPATH, "//*[contains(text(),'Remove')]")
    item_quantity = (By.XPATH, "//select[contains(@id, 'quantityselect')]")
    add_cart_button= (By.XPATH,"//button[contains(@class,'addToCartButton')]/child::span[contains(@class,'prefix-btn')]")
    go_cart_link = (By.XPATH,"//div[contains(@class,'prefix-toast')]/descendant::button[contains(@class,'prefix-toast__action-message')]")

    def create_list(self):
        return WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located(self.new_list)))

    def set_list_name(self):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.list_name)))

    def do_rename_list(self):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.rename_list)))

    def do_save_list(self):
        return WebDriverWait(self.driver,10).until((EC.visibility_of_element_located(self.save_list)))

    def close_confirm_alert(self):
        WebDriverWait(self.driver,30).until((EC.visibility_of_element_located(self.confirm_alert))).click()

    def text_on_alert(self, text):
        try:
            WebDriverWait(self.driver, 30).until(
                EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), '" + text + "')]")))
            return True
        except TimeoutException:
            return False

    def click_list_actions_button(self):
        time.sleep(3)
        element = WebDriverWait(self.driver, 30).until((EC.visibility_of_element_located(self.list_actions_button)))
        return element

    def move_items_to_other_list(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.move_items_link)))

    def do_create_new_list(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.new_list2)))

    def move_items_new_list(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.vmove_items_new_list)))

    def click_view_link(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.view_link))

    def click_back_to_lists_button(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.back_to_lists)))

    def click_list1_name_link(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.list1_name_link)))

    def click_list2_name_link(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.list2_name_link)))

    def click_list_options(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.list_options)))

    def click_remove_list_link(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.remove_list_link)))

    def click_remove_button(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.remove_button)))

    def click_change_list_link(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.change_list_link)))

    def click_on_quantity(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.item_quantity)))

    def select_item_quantity(self,text):
        sel = Select(self.click_on_quantity())
        sel.select_by_visible_text(text)

    def add_all_items_to_cart(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.add_cart_button)))

    def click_go_cart_link(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.go_cart_link)))

