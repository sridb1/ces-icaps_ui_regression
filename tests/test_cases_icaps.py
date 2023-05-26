import time
import pytest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.CartPage import CartPage
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from pages.ProductInfoPage import ProductInfoPage
from pages.ProfilePage import ProfilePage
from pages.ShoppingListPage import ShoppingListPage
from pages.SignupPage import SignupPage
from test_data.loadexceldata import LoadExcelData
from utilities.BaseClass import BaseClass


class TestFlow(BaseClass):

    random_string = BaseClass.generate_random_string(8)
    v_email = 'test' + random_string + '@mailinator.com'

    @pytest.mark.temp
    @pytest.mark.profiles
    @pytest.mark.run(order=1)
    def test_signup(self, getData):
        log = self.getLogger()
        self.driver.get(str(getData["url"]) + "/profile/sign-up")
        self.login_ingka_profile(getData)
        home_page = HomePage(self.driver)
        signup=SignupPage(self.driver)
        home_page.accept_cookies().click()
        self.clear_popup()
        signup.set_firstname(getData["firstname"])
        signup.set_lastname(getData["lastname"])
        # signup.set_email(getData["loginuser"])
        signup.set_email(self.v_email)
        log.info('email generated: '+self.v_email)
        signup.set_password(getData["loginpwd"])
        signup.select_privacy_checkbox()
        signup.do_submit().click()
        time.sleep(5)
        # assert True == signup.validate_check_point()
        # log.info("Profile is created successfully")

    @pytest.mark.temp
    def t1est_temp(self, getData):
        log = self.getLogger()
        profile = ProfilePage(self.driver)
        login = LoginPage(self.driver)
        """sign up new profile"""
        self.test_signup(getData)
        self.driver.execute_script("window.open('about:blank', 'secondtab');")
        self.driver.switch_to.window('secondtab')
        self.driver.get(str(getData["url"]) + "/profile/login")
        # assert True == login.validate_check_point()
        # self.do_click(profile.logout)
        log.info("logged out in duplicate session")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(str(getData["url"]) + "/profile/login")
        # assert True == WebDriverWait(self.driver, 30).until(
        #     EC.visibility_of_element_located(login.email)).is_displayed()

        """login again in first tab"""
        self.driver.get(str(getData["url"]) + "/profile/login")
        # login.set_email(getData["loginuser"])
        login.set_email(self.v_email)
        login.set_password(getData["loginpwd"])
        login.do_submit().click()
        assert True == login.validate_check_point()
        log.info("Profile login successful")
        self.driver.switch_to.window('secondtab')
        self.driver.get(str(getData["url"]) + "/profile/login")
        profile.do_delete_account().click()
        profile.set_password(getData["loginpwd"])
        profile.do_submit().click()
        assert True == self.validate_url_check_point('profile/account-deleted')
        log.info("Profile is Deleted successfully")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(str(getData["url"]) + "/profile/login")
        assert True == WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(login.email)).is_displayed()

    @pytest.mark.profiles
    @pytest.mark.run(order=2)
    def test_edit_profile(self, getData):
        log = self.getLogger()
        v_url = getData['url']
        profile = ProfilePage(self.driver)
        self.login(getData)
        profile.view_profile_details().click()
        profile.do_edit_personal_info().click()
        profile.edit_first_name('Edward')
        profile.edit_last_name('Sagan')
        if 'mx/en' in v_url:
            profile.edit_phone('353 453 4556')
        # elif 'ph/en' in v_url:
        #     profile.edit_phone('445545533')
        profile.do_save()
        # added below temporarily
        if 'jo/en' in v_url:
            pass
        else:
            assert True == profile.validate_check_point()
        log.info("Personal information updated")

        """add address information"""
        if 'mx/en' in v_url:
            profile.click_add_address_btn()
            # profile.edit_first_name('abraham')
            # profile.edit_last_name('kher')
            profile.add_address_line1('AVE. PALACE OF JUSTICE 44')
            profile.add_city('Mexico')
            profile.add_postal_code('66450')
            profile.edit_phone('353 459 4556')
            profile.do_save()
            log.info("address information added")

        elif 'ph/en' in v_url:
            profile.click_add_address_btn()
            profile.edit_first_name('Lynn')
            profile.edit_last_name('Lynn')
            profile.edit_phone('445545533')
            profile.select_region()
            profile.select_city()
            profile.select_barangay()
            profile.add_address_line1('RONALDO CHAMBER STREET 22')
            # profile.add_city('Manila')
            # profile.add_postal_code('66450')
            # profile.edit_phone('445545533')
            profile.do_save()
            log.info("address information added")

    @pytest.mark.profiles
    @pytest.mark.run(order=3)
    def test_update_password(self, getData):
        log = self.getLogger()
        self.login(getData)
        profile = ProfilePage(self.driver)
        login = LoginPage(self.driver)
        """update new password"""
        profile.do_change_password().click()
        profile.set_current_password(getData['loginpwd'])
        profile.set_new_password(getData['loginpwd'] + '*')
        profile.set_confirm_password(getData['loginpwd'] + '*')
        profile.do_submit().click()
        assert True == profile.validate_check_point()
        log.info("Password is updated")
        self.logout(getData)

        """verify Authentication with new password"""
        self.driver.get(str(getData["url"]) + "/profile/login")
        # login.set_email(getData["loginuser"])
        login.set_email(self.v_email)
        login.set_password(getData["loginpwd"] + '*')
        login.do_submit().click()
        assert True == login.validate_check_point()
        log.info("Profile Login is Successfully with new password")

        """Updating Password to previous one to use same credentials for next test cases"""
        profile.do_change_password().click()
        profile.set_current_password(getData['loginpwd'] + '*')
        profile.set_new_password(getData['loginpwd'])
        profile.set_confirm_password(getData['loginpwd'])
        profile.do_submit().click()
        self.logout(getData)

    @pytest.mark.run(order=4)
    def test_forgot_password(self, getData):
        log = self.getLogger()
        home_page = HomePage(self.driver)
        login = LoginPage(self.driver)
        # user_name = getData["loginuser"].split("@")
        user_name = self.v_email.split("@")
        email2 = user_name[0] + 'new@' + user_name[1]
        self.driver.get(str(getData["url"]) + "/profile/sign-up")
        self.login_ingka_profile(getData)
        signup = SignupPage(self.driver)
        home_page.accept_cookies().click()
        self.clear_popup()
        signup.set_firstname(getData["firstname"])
        signup.set_lastname(getData["lastname"])
        signup.set_email(email2)
        signup.set_password(getData["loginpwd"])
        signup.select_privacy_checkbox()
        signup.do_submit().click()
        assert True == signup.validate_check_point()
        login.do_click(login.logout)
        self.driver.get(str(getData["url"]) + "/profile/login")
        login.click_forgot_pwd_link()
        login.set_email(email2)
        login.do_submit().click()
        # assert True == self.validate_url_check_point('reset/success')
        log.info("reset password page displayed")

    @pytest.mark.smoke
    @pytest.mark.run(order=5)
    def test_list_with_registered_user(self, getData):
        log = self.getLogger()
        wishlist = ShoppingListPage(self.driver)
        home_page = HomePage(self.driver)
        product_info_page = ProductInfoPage(self.driver)
        self.login(getData)
        self.driver.get(str(getData["url"]) + "/favourites/")
        self.login_ingka_profile(getData)
        self.clear_popup()
        wishlist.create_list().click()
        wishlist.set_list_name().send_keys('ShoppingList1')
        wishlist.do_save_list().click()
        assert True == wishlist.text_on_alert('created')
        wishlist.close_confirm_alert()
        log.info("New Shopping list is created")
        self.press_home_key()
        home_page.do_search_items().click()
        home_page.do_search_items().send_keys('ikea')
        home_page.click_search_button()
        home_page.add_products_to_list(1).click()
        home_page.add_products_to_list(2).click()
        home_page.click_view_link().click()
        assert True == self.validate_url_check_point('favourites')
        log.info("Items are added to shopping list from search results page")

        """search another item and go to Product info page(PIP)"""
        home_page.do_search_items().send_keys('ikea')
        home_page.click_search_button()
        home_page.do_click_on_product().click()
        assert True == self.validate_url_check_point('/p/')
        log.info("Product info page is displayed")
        product_info_page.click_favourite_button()
        product_info_page.click_view_link().click()
        self.clear_popup()
        wishlist.click_list_actions_button().click()
        wishlist.move_items_to_other_list().click()
        wishlist.do_create_new_list().click()
        wishlist.set_list_name().send_keys('ShoppingList2')
        wishlist.do_save_list().click()
        assert True == wishlist.text_on_alert('created')
        wishlist.close_confirm_alert()
        log.info("Second Shoppinglist is created")
        wishlist.move_items_new_list().click()
        wishlist.click_view_link().click()
        log.info("Item moved to second shopping list")

        """Remove 1st shopping list"""
        wishlist.click_back_to_lists_button().click()
        wishlist.click_list1_name_link().click()
        wishlist.click_list_options().click()
        wishlist.click_remove_list_link().click()
        wishlist.click_remove_button().click()
        log.info("first shopping list is removed")

        """Change shopping list name"""
        wishlist.click_list2_name_link().click()
        wishlist.click_list_options().click()
        wishlist.click_change_list_link().click()
        wishlist.do_rename_list().clear()
        wishlist.do_rename_list().send_keys('MyWishList')
        wishlist.do_save_list().click()
        wishlist.close_confirm_alert()
        log.info("shopping list name is changed")
        wishlist.click_on_quantity().click()
        wishlist.select_item_quantity('4')
        log.info("Item count is modified")
        wishlist.add_all_items_to_cart().click()
        wishlist.click_go_cart_link().click()
        assert True == self.validate_url_check_point('cart')
        log.info("Item moved to shopping cart")

    @pytest.mark.trial
    @pytest.mark.run(order=6)
    def test_cart_with_registered_user(self, getData):
        log = self.getLogger()
        self.login(getData)
        home_page = HomePage(self.driver)
        product_info_page = ProductInfoPage(self.driver)
        shopping_cart = CartPage(self.driver)
        self.driver.get(str(getData["url"]))
        self.login_ingka_profile(getData)
        self.clear_popup()
        home_page.do_search_items().send_keys('ikea')
        home_page.click_search_button()
        home_page.add_products_to_cart('3').click()
        home_page.add_products_to_cart('4').click()
        home_page.add_products_to_cart('5').click()
        home_page.click_go_cart_link().click()
        log.info("Products are added to shopping cart from results page")
        assert True == self.validate_url_check_point('cart')
        self.clear_popup()
        shopping_cart.do_remove_item().click()
        shopping_cart.close_confirm_alert()
        # assert 'Undo' in shopping_cart.get_text_value(shopping_cart.undo_link)
        log.info("Item removed")

        """move an item to favourites"""
        shopping_cart.do_save_favourites().click()
        shopping_cart.click_view_link().click()
        assert True == self.validate_url_check_point('favourites')
        log.info("Item moved to favourites")

        """search another item and go to Product info page(PIP)"""
        home_page.do_search_items().send_keys('ikea')
        home_page.click_search_button()
        home_page.do_click_on_product().click()
        assert True == self.validate_url_check_point('/p/')
        log.info("Product info page is displayed")
        self.clear_popup()
        product_info_page.click_cart_btn().click()
        product_info_page.click_continue_cart_link()
        self.clear_popup()
        assert True == self.validate_url_check_point('cart')
        log.info("Products moved to cart from PIP")
        # shopping_cart.select_item_quantity('4')
        shopping_cart.click_checkout_btn()
        assert True == self.validate_url_check_point('checkout')
        log.info("checkout page is displayed")

    @pytest.mark.profiles
    @pytest.mark.run(order=7)
    def test_profile_delete(self, getData):
        log = self.getLogger()
        profile = ProfilePage(self.driver)
        self.login(getData)
        time.sleep(5)
        self.driver.get(str(getData["url"]) + "/profile/login")
        profile.do_delete_account().click()
        profile.set_password(getData["loginpwd"])
        profile.do_submit().click()
        assert True == self.validate_url_check_point('profile/account-deleted')
        log.info("Profile is Deleted successfully")

    @pytest.mark.run(order=8)
    def test_list_with_guest(self, getData):
        log = self.getLogger()
        wishlist = ShoppingListPage(self.driver)
        home_page = HomePage(self.driver)
        product_info_page = ProductInfoPage(self.driver)
        self.driver.get(str(getData["url"]) + "/favourites/")
        self.login_ingka_profile(getData)
        home_page.accept_cookies().click()
        self.clear_popup()
        wishlist.create_list().click()
        wishlist.set_list_name().send_keys('ShoppingList1')
        wishlist.do_save_list().click()
        log.info("New Shopping list is created")
        assert True == wishlist.text_on_alert('created')
        wishlist.close_confirm_alert()
        self.press_home_key()
        home_page.do_search_items().click()
        home_page.do_search_items().send_keys('ikea')
        home_page.click_search_button()
        home_page.add_products_to_list(1).click()
        home_page.add_products_to_list(2).click()
        home_page.click_view_link().click()
        assert True == self.validate_url_check_point('favourites')
        log.info("Items are added to shopping list from search results page")

        """search another item and go to Product info page(PIP)"""
        home_page.do_search_items().send_keys('ikea')
        home_page.click_search_button()
        home_page.do_click_on_product().click()
        assert True == self.validate_url_check_point('/p/')
        log.info("Product info page is displayed")
        product_info_page.click_favourite_button()
        product_info_page.click_view_link().click()
        self.clear_popup()
        wishlist.click_list_actions_button().click()
        wishlist.move_items_to_other_list().click()
        wishlist.do_create_new_list().click()
        wishlist.set_list_name().send_keys('ShoppingList2')
        wishlist.do_save_list().click()
        assert True == wishlist.text_on_alert('created')
        wishlist.close_confirm_alert()
        log.info("Second Shoppinglist is created")
        wishlist.move_items_new_list().click()
        wishlist.click_view_link().click()
        log.info("Item moved to second shopping list")

        """Remove 1st shopping list"""
        wishlist.click_back_to_lists_button().click()
        wishlist.click_list1_name_link().click()
        wishlist.click_list_options().click()
        wishlist.click_remove_list_link().click()
        wishlist.click_remove_button().click()
        log.info("first shopping list is removed")

        """Change shopping list name"""
        wishlist.click_list2_name_link().click()
        wishlist.click_list_options().click()
        wishlist.click_change_list_link().click()
        wishlist.do_rename_list().clear()
        wishlist.do_rename_list().send_keys('MyWishList')
        wishlist.do_save_list().click()
        wishlist.close_confirm_alert()
        log.info("shopping list name is changed")
        wishlist.click_on_quantity().click()
        wishlist.select_item_quantity('4')
        log.info("Item count is modified")
        wishlist.add_all_items_to_cart().click()
        wishlist.click_go_cart_link().click()
        assert True == self.validate_url_check_point('cart')
        log.info("Item moved to shopping cart")

    @pytest.mark.run(order=9)
    def test_cart_with_guest(self, getData):
        log = self.getLogger()
        wishlist = ShoppingListPage(self.driver)
        home_page = HomePage(self.driver)
        login = LoginPage(self.driver)
        product_info_page = ProductInfoPage(self.driver)
        shopping_cart = CartPage(self.driver)
        self.driver.get(str(getData["url"]))
        self.login_ingka_profile(getData)
        home_page.accept_cookies().click()
        self.clear_popup()
        home_page.do_search_items().send_keys('ikea')
        home_page.click_search_button()
        home_page.add_products_to_cart('3').click()
        home_page.add_products_to_cart('4').click()
        home_page.add_products_to_cart('5').click()
        home_page.click_go_cart_link().click()
        log.info("Products are added to shopping cart from results page")
        assert True == self.validate_url_check_point('cart')
        self.clear_popup()
        shopping_cart.do_remove_item().click()
        shopping_cart.close_confirm_alert()
        # assert 'Undo' in shopping_cart.get_text_value(shopping_cart.undo_link)
        log.info("Item removed")

        """move an item to favourites"""
        shopping_cart.do_save_favourites().click()
        shopping_cart.click_view_link().click()
        assert True == self.validate_url_check_point('favourites')
        log.info("Item moved to favourites")

        """search another item and go to Product info page(PIP)"""
        home_page.do_search_items().send_keys('ikea')
        home_page.click_search_button()
        home_page.do_click_on_product().click()
        # self.clear_popup()
        assert True == self.validate_url_check_point('/p/')
        log.info("Product info page is displayed")
        product_info_page.click_cart_btn().click()
        self.clear_popup()
        product_info_page.click_continue_cart_link()
        # assert True == shopping_cart.validate_url_check_point()
        assert True == self.validate_url_check_point('cart')
        log.info("Products moved to cart from PIP")
        # shopping_cart.select_item_quantity('4')
        shopping_cart.click_checkout_btn()
        assert True == self.validate_url_check_point('checkout')
        log.info("checkout page is displayed")

    @pytest.mark.profile
    @pytest.mark.run(order=10)
    def test_duplicate_session(self, getData):
        log = self.getLogger()
        profile = ProfilePage(self.driver)
        login = LoginPage(self.driver)
        """sign up new profile"""
        self.test_signup(getData)
        self.driver.execute_script("window.open('about:blank', 'secondtab');")
        self.driver.switch_to.window('secondtab')
        self.driver.get(str(getData["url"]) + "/profile/login")
        # assert True == login.validate_check_point()
        # self.do_click(profile.logout)
        log.info("logged out in duplicate session")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(str(getData["url"]) + "/profile/login")
        # assert True == WebDriverWait(self.driver, 30).until(
        #     EC.visibility_of_element_located(login.email)).is_displayed()

        """login again in first tab"""
        self.driver.get(str(getData["url"]) + "/profile/login")
        # login.set_email(getData["loginuser"])
        login.set_email(self.v_email)
        login.set_password(getData["loginpwd"])
        login.do_submit().click()
        assert True == login.validate_check_point()
        log.info("Profile login successful")
        self.driver.switch_to.window('secondtab')
        self.driver.get(str(getData["url"]) + "/profile/login")
        profile.do_delete_account().click()
        profile.set_password(getData["loginpwd"])
        profile.do_submit().click()
        assert True == self.validate_url_check_point('profile/account-deleted')
        log.info("Profile is Deleted successfully")
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.get(str(getData["url"]) + "/profile/login")
        assert True == WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(login.email)).is_displayed()

    @pytest.fixture(params=LoadExcelData.getTestData("Testcase1"))
    def getData(self, request):
        return request.param



