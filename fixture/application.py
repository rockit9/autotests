from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


class Application:

    def __init__(self):
            self.driver = webdriver.Chrome(ChromeDriverManager().install())
            self.driver.implicitly_wait(10)

    def open_main_page(self):
        driver = self.driver
        driver.get("https://givehope.abz.agency/")

    def start_campaign_creation_unauthorised_user(self):
        driver = self.driver
        driver.find_element_by_css_selector("a[ampsendevent='start_fundraiser']").click()

    def destroy(self):
        self.driver.quit()
