
from selenium import webdriver


class Application:

    def __init__(self):
            self.driver = webdriver.Chrome(executable_path="C://drivers/chromedriver.exe")
            self.driver.implicitly_wait(10)
            

    def go_to_booking(self):
        driver = self.driver
        driver.find_element_by_link_text("Тайная личность").click()
        driver.find_element_by_css_selector(
            "#content > div.container-wrapper.quests > div.schedule > div > div > div:nth-child(1) > div.row.no-url > div.shedule-blocks > div.new-wrapper > div:nth-child(1) > div.td-wrap > div:nth-child(6)").click()

    def open_booking_page(self):
        driver = self.driver
        driver.get("https://qg3.abz.agency/raspisanie-kvestov-kiev")

    def destroy(self):
        self.driver.quit()
