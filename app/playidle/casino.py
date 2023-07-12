from selenium import webdriver
from selenium.webdriver.common.by import By

from playidle.bank import Bank
from playidle.playidle_base_class import Base


class Casion(Base):
    def __init__(
        self, driver: webdriver, page_urls: dict[str, str], element_ids: dict[str, str]
    ):
        super().__init__(driver, page_urls, element_ids)
        self.bank = Bank(self.driver, self.page_urls, self.element_ids)

    def coin_flip(self):
        """
        Flips a coin.

        This function navigates to the coinflip page and performs a coin flip.

        """
        self.nav.go_to_page(self.page_urls["coinflip"])

        job_button = self.driver.find_element(By.ID, self.element_ids["wager"])

        job_button.click()

        self.nav.wait_for_page()
