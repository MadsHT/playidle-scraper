from playidle.playidle_base_class import Base

from selenium import webdriver
from selenium.webdriver.common.by import By


class Player(Base):
    def __init__(
        self, driver: webdriver, page_urls: dict[str, str], element_ids: dict[str, str]
    ):
        super().__init__(driver, page_urls, element_ids)

    def get_wallet_amount(self) -> int:
        """
        Get the amount of money currently in the user's wallet.

        Returns:
            int: The amount of money in the wallet.
        """
        wallet_amount_element = self.driver.find_element(
            By.ID, self.element_ids["wallet_amount_element"]
        )

        return int(
            wallet_amount_element.get_attribute("textContent").replace(",", "")
            if "," in wallet_amount_element.get_attribute("textContent")
            else wallet_amount_element.get_attribute("textContent")
        )

    def get_energy(self) -> int:
        """
        Get the energy value from the web page.

        Returns:
            int: The energy value as an integer.
        """

        energy_element = self.driver.find_element(
            By.ID, self.element_ids["energy_element"]
        )

        return int(energy_element.get_attribute("textContent"))
