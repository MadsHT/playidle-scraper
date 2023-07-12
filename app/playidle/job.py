from selenium import webdriver
from selenium.webdriver.common.by import By

from playidle.playidle_base_class import Base


class Job(Base):
    def __init__(
        self, driver: webdriver, page_urls: dict[str, str], element_ids: dict[str, str]
    ):
        super().__init__(driver, page_urls, element_ids)

    def click_job(self):
        """
        Clicks on the job button after navigating to the dashboard page.

        """
        self.nav.go_to_page(self.page_urls["dashboard"])

        job_button = self.driver.find_element(By.ID, self.element_ids["job_button"])

        job_button.click()

        # This does not really do antything, since this waits for the page to be fully loaded
        # What we really need here is to wait for all requests to be completed the problem is that
        # we have the same request every time
        self.nav.wait_for_page()
