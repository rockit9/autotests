import time

from selenium.common.exceptions import ElementNotVisibleException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def reg_with_fb(self, mail, password):
        driver = self.app.driver
        driver.find_element_by_css_selector("a[ampsendevent='start_fundraiser']").click()
        # fb_button = WebDriverWait(driver, 10).until(
        #   EC.element_to_be_clickable((By.TAG_NAME, "facebook-native-button")))
        fb_button = driver.find_element_by_tag_name("facebook-native-button")
        time.sleep(3)
        fb_button.click()
        time.sleep(3)
        windows_list = driver.window_handles
        driver.switch_to.window(windows_list[1])
        driver.find_element_by_css_selector("#email").click()
        driver.find_element_by_css_selector("#email").send_keys(mail)
        driver.find_element_by_css_selector("#pass").click()
        driver.find_element_by_css_selector("#pass").send_keys(password)
        driver.find_element_by_css_selector("#loginbutton").click()
        driver.switch_to.window(windows_list[0])

    def log_with_fb(self, mail, password):
        driver = self.app.driver
        driver.find_element_by_css_selector("header > div > div.header-left > hamburger > div").click()
        driver.find_element_by_css_selector("user-menu > div > ul > li:nth-child(5) > a").click()
        time.sleep(2)
        driver.find_element_by_tag_name("facebook-native-button").click()
        time.sleep(3)
        windows_list = driver.window_handles
        driver.switch_to.window(windows_list[1])
        driver.find_element_by_css_selector("#email").click()
        driver.find_element_by_css_selector("#email").send_keys(mail)
        driver.find_element_by_css_selector("#pass").click()
        driver.find_element_by_css_selector("#pass").send_keys(password)
        driver.find_element_by_css_selector("#loginbutton").click()
        driver.switch_to.window(windows_list[0])

    def check_is_reg_page(self):
        driver = self.app.driver
        time.sleep(1)
        get_text = driver.find_element_by_css_selector("div.start-company-header__text")
        assert get_text.text == "Hi Mahatma, enter your goal"

    def check_is_logged_in(self):
        driver = self.app.driver
        time.sleep(3)
        get_text = driver.find_element_by_css_selector("header > div > div.header-right.ng-star-inserted > a")
        assert get_text.text == "Dashboard"

    def logout(self):
        driver = self.app.driver
        try:
            driver.find_element_by_css_selector("header > div > div.header-right > div > div").click()
            logout_button = driver.find_element_by_xpath("//*[.='Sign Out']")
        except ElementNotVisibleException:
            driver.find_element_by_css_selector("header > div > div.header-left > hamburger > div").click()
            logout_button = driver.find_element_by_css_selector("ul.ng-tns-c6-25.ng-star-inserted li.header-desktop-menu__li:nth-child(10) > a.header-desktop-menu__link")

        logout_button.click()
