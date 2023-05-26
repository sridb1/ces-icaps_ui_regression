from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductInfoPage:

    def __init__(self,driver):
        self.driver = driver

    favourite_btn = "(//button[contains(@class,'favourite-button')])[position()=1]"
    # cart_btn = (By.XPATH, "//span[contains(text(),'Add to cart')]")
    cart_btn = (By.XPATH, "//button[contains(@class,'pip-btn pip-btn--emphasised')]")
    view_link = (By.XPATH, "//button[contains(@aria-label,'View')]//span[contains(@class,'prefix-btn__inner')]")

    def click_favourite_button(self):
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.favourite_btn))

    def click_view_link(self):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.view_link))

    def click_cart_btn(self):
        return WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.cart_btn))

    def click_continue_cart_link(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='rec-added-to-cart__hero']/child::a[starts-with(text(),'Continue')]"))).click()
        except NoSuchElementException:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='pip-btn pip-btn--emphasised']//span[@class='pip-btn__inner']"))).click()
