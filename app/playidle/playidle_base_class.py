from playidle.navigation import Navigation
from selenium import webdriver


class Base:
    def __init__(
        self,
        driver: webdriver.Chrome,
        page_urls: dict[str, str],
        element_ids: dict[str, str],
    ):
        self.driver = driver
        self.page_urls = page_urls
        self.element_ids = element_ids

        self.nav = Navigation(self.driver, self.page_urls)
