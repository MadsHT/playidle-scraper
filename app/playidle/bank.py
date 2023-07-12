from playidle.playidle_base_class import Base

from selenium import webdriver
from selenium.webdriver.common.by import By


class Bank(Base):
    def __init__(
        self,
        driver: webdriver.Chrome,
        page_urls: dict[str, str],
        element_ids: dict[str, str],
    ):
        super().__init__(driver, page_urls, element_ids)

    def __perform_transaction(self, button_id: str, input_id: str) -> int:
        """
        Perform a transaction by clicking a button and submitting a form.

        Args:
            button_id (str): The ID of the button to be clicked.
            input_id (str): The ID of the input field containing the value to be returned.
            redirect_to (str, optional): The URL to redirect to after submitting the form.

        Returns:
            int: The value of the input field, parsed as an integer after removing commas.
        """
        self.nav.go_to_page(self.page_urls["bank"])

        # Find the button
        submit_button = self.driver.find_element(By.ID, button_id)

        input_value = self.driver.find_element(By.ID, input_id).get_attribute("value")

        # Submit the login form
        submit_button.click()

        # Wait for the request to complete
        self.nav.wait_for_page()

        return int(input_value.replace(",", ""))

    def deposit_money(self) -> int:
        """
        Deposits money into the bank account.

        Returns:
            int: The amount of money that was deposited.
        """
        deposit_button_id = self.element_ids["deposit_button"]
        deposit_input_id = self.element_ids["deposit_input"]

        return self.__perform_transaction(deposit_button_id, deposit_input_id)

    def withdraw_money(self) -> int:
        """
        Withdraws money from the bank account.

        Returns:
            int: The amount of money that was withdrawn.
        """
        withdraw_button_id = self.element_ids["withdraw_button"]
        withdraw_input_id = self.element_ids["withdraw_input"]

        return self.__perform_transaction(withdraw_button_id, withdraw_input_id)
