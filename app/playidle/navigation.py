from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


class Navigation:
    def __init__(
        self,
        driver: webdriver.Chrome,
        page_urls: dict[str, str],
    ):
        self.driver = driver
        self.page_urls = page_urls

    def go_to_page(self, url: str):
        """
        Navigates to the specified URL if it is not already the current URL.

        Args:
            url (str): The URL to navigate to.

        """
        if url not in self.driver.current_url:
            self.driver.get(url)
            self.wait_for_page()

    def wait_for_page(self):
        """
        Wait for the page to fully load.

        This function waits for the page to fully load by using a WebDriverWait object
        with a timeout of 10 seconds. It checks the readyState of the document using
        JavaScript to determine if the page has fully loaded.
        """
        wait = WebDriverWait(self.driver, 10)

        def page_fully_loaded(driver):
            return driver.execute_script("return document.readyState") == "complete"

        wait.until(page_fully_loaded)
