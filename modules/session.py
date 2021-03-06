# -*- coding: utf-8 -*-


import time
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def reg_with_fb(self, mail, password):
        driver = self.app.driver
        SessionHelper.check_current_loc(self)
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
        driver.find_element_by_link_text("Sign In").click()
        time.sleep(2)
        driver.find_element_by_tag_name("facebook-native-button").click()
        time.sleep(2)
        windows_list = driver.window_handles
        if len(windows_list) > 1:
            driver.switch_to.window(windows_list[1])
            driver.find_element_by_css_selector("#email").click()
            driver.find_element_by_css_selector("#email").send_keys(mail)
            driver.find_element_by_css_selector("#pass").click()
            driver.find_element_by_css_selector("#pass").send_keys(password)
            driver.find_element_by_css_selector("#loginbutton").click()
            driver.switch_to.window(windows_list[0])

    def check_current_loc(self):
        driver = self.app.driver
        try:
            driver.find_element_by_link_text("Start a FREE Fundraiser")
            loc = "en"
        except NoSuchElementException:
            loc = "ru"
        return loc

    def switch_to_another_local(self, lang="en"):
        driver = self.app.driver
        driver.find_element_by_css_selector("div.footer-block-select-wrap").click()
        driver.find_element_by_css_selector("languages-select > select > option[value= " + lang + "] ").click()

    def reg_with_vk(self, mail, password):
        driver = self.app.driver
        driver.find_element_by_css_selector("a[ampsendevent='start_fundraiser']").click()
        # fb_button = WebDriverWait(driver, 10).until(
        #   EC.element_to_be_clickable((By.TAG_NAME, "facebook-native-button")))
        vk_button = driver.find_element_by_tag_name("social-vkontakte-button")
        time.sleep(2)
        vk_button.click()
        time.sleep(2)
        windows_list = driver.window_handles
        driver.switch_to.window(windows_list[1])
        driver.find_element_by_css_selector("input[name='email']").click()
        driver.find_element_by_css_selector("input[name='email']").send_keys(mail)
        driver.find_element_by_css_selector("input[name='pass']").click()
        driver.find_element_by_css_selector("input[name='pass']").send_keys(password)
        driver.find_element_by_css_selector("button[type='submit']").click()
        driver.switch_to.window(windows_list[0])

    def log_with_vk(self, mail, password):
        driver = self.app.driver
        driver.find_element_by_css_selector("header > div > div.header-left > hamburger > div").click()
        driver.find_element_by_link_text("Войти в систему").click()
        time.sleep(2)
        driver.find_element_by_tag_name("social-vkontakte-button").click()
        time.sleep(3)
        windows_list = driver.window_handles
        if len(windows_list) > 1:
            driver.switch_to.window(windows_list[1])
            driver.find_element_by_css_selector("input[name='email']").click()
            driver.find_element_by_css_selector("input[name='email']").send_keys(mail)
            driver.find_element_by_css_selector("input[name='pass']").click()
            driver.find_element_by_css_selector("input[name='pass']").send_keys(password)
            driver.find_element_by_css_selector("button[type='submit']").click()
            driver.switch_to.window(windows_list[0])

    def check_is_reg_page_fb(self):
        driver = self.app.driver
        time.sleep(1)
        get_text = driver.find_element_by_css_selector("div.start-company-header__text")
        assert get_text.text == "Hi Pindamonhangaba, enter your goal"

    def check_is_logged_in_fb(self):
        driver = self.app.driver
        get_text = driver.find_element_by_css_selector("header > div > div.header-right.ng-star-inserted > a")
        assert get_text.text == "Dashboard" or "Start a FREE Fundraiser"

    def check_is_reg_page_vk(self):
        driver = self.app.driver
        text = driver.find_element_by_css_selector(" form > div.start-company-form-contant > div.form-group > label")
        assert text.text == "Название моей кампании"

    def check_is_logged_in_vk(self):
        driver = self.app.driver
        driver.find_element_by_css_selector("header > div > div.header-left > hamburger > div").click()
        text = driver.find_element_by_link_text("Выход")
        assert text.text == "Выход"
        driver.find_element_by_css_selector("header > div > div.header-left > hamburger > div").click()

    def logout_fb(self):
        driver = self.app.driver
        try:
            driver.find_element_by_css_selector("header > div > div.header-right > div > div").click()
            driver.find_element_by_link_text("Sign Out").click()
        except ElementNotVisibleException:
            driver.find_element_by_css_selector("header > div > div.header-left > hamburger > div").click()
            driver.find_element_by_link_text("Sign Out").click()

    def logout_vk(self):
        driver = self.app.driver
        try:
            driver.find_element_by_css_selector("div.header-right > div").click()
            driver.find_element_by_link_text("Выход").click()
        except ElementNotVisibleException:
            driver.find_element_by_css_selector("header > div > div.header-left > hamburger > div").click()
            driver.find_element_by_link_text("Выход").click()
