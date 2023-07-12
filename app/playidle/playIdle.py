from selenium.webdriver.common.by import By
from playidle.job import Job
from playidle.bank import Bank
from playidle.casino import Casion
from playidle.player import Player
from playidle.playidle_base_class import Base


class PlayIdle(Base):
    def __init__(self, driver, page_urls, element_ids):
        super().__init__(driver, page_urls, element_ids)

        self.player = Player(self.driver, self.page_urls, self.element_ids)
        self.bank = Bank(self.driver, self.page_urls, self.element_ids)
        self.casino = Casion(self.driver, self.page_urls, self.element_ids)
        self.job = Job(self.driver, self.page_urls, self.element_ids)

    def login(self, username: str, password: str) -> bool:
        """
        Logs into a website using the provided credentials.

        Args:
            url (str): The URL of the login page.
            username (str): The username to login with.
            password (str): The password to login with.

        Returns:
            bool: True if the login was successful, False otherwise.
        """

        # Load the login page
        self.nav.go_to_page(self.page_urls["login"])

        # Find the username and password input fields and submit button
        username_input = self.driver.find_element(By.NAME, self.element_ids["username"])
        password_input = self.driver.find_element(By.NAME, self.element_ids["password"])
        submit_button = self.driver.find_element(
            By.ID, self.element_ids["submit_button"]
        )

        # Fill in the login form
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit the login form
        submit_button.click()

        self.nav.wait_for_page()

        # Check if the login was successful
        return "dashboard" in self.driver.current_url
