from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from modules.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_main_page(self):
        driver = self.driver
        driver.get("https://givehope.abz.agency/")

    def destroy(self):
        self.driver.quit()
