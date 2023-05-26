from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage:

    def __init__(self,driver):
        self.driver = driver

    accept_cookies_btn = (By.XPATH, "//button[@id='onetrust-accept-btn-handler'or contains(@class,'accept-button')]")
    search_items = (By.XPATH, "//input[contains(@name,'q')]")
    search_button = (By.XPATH, "//button[@id='search-box__searchbutton']")
    click_on_product = (By.XPATH, "(//span[contains(@class,'notranslate')])[position()=6]")
    view_link = (By.XPATH, "//button[contains(@aria-label,'View')]//span[contains(@class,'prefix-btn__inner')]")
    # go_cart_link = (By.XPATH,"//button[contains(@aria-label,'cart')]//span[contains(@class,'prefix-btn__inner')]")
    go_cart_link = (By.XPATH,"//button[contains(@aria-label,'Go to')]")
    favourite_btn = "(//button[contains(@aria-label,'rites')])[position()=1]"

    def accept_cookies(self):
        try:
            # wait= self.driver.find_element(*LoginPage.cookieAccept)
            return WebDriverWait(self.driver, 30).until((EC.element_to_be_clickable(self.accept_cookies_btn)))
        except (NoSuchElementException,ElementClickInterceptedException):
            pass

    def do_search_items(self):
        return WebDriverWait(self.driver,20).until((EC.visibility_of_element_located(self.search_items)))

    def click_search_button(self):
        WebDriverWait(self.driver,10).until((EC.visibility_of_element_located(self.search_button))).click()

    # def click_favourite_button(self):
    #     self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.favourite_btn))

    def add_products_to_list(self,position):
        # return WebDriverWait(self.driver,30).until((EC.visibility_of_element_located((By.XPATH,"(//button[contains(@aria-label,'Save to') or contains(@aria-label,'Add to fav')]) [position()='%s']"%str(position)))))
        return WebDriverWait(self.driver,30).until((EC.visibility_of_element_located((By.XPATH,"(//button[contains(@aria-label,'Save to shopping') or contains(@aria-label,'to fav')]) [position()='%s']"%str(position)))))
        # self.driver.execute_script("arguments[0].click();", self.driver.find_element(self.favourite_btn))

    def add_products_to_cart(self,position):
        return WebDriverWait(self.driver,30).until((EC.visibility_of_element_located((By.XPATH, "(//button[contains(@class,'add-to-cart-button') or contains(@aria-label,'Add to cart')])[position()="+str(position)+"]"))))

    def click_view_link(self):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.view_link)))

    def click_go_cart_link(self):
        return WebDriverWait(self.driver, 20).until((EC.visibility_of_element_located(self.go_cart_link)))

    def do_click_on_product(self):
        return WebDriverWait(self.driver, 10).until((EC.visibility_of_element_located(self.click_on_product)))