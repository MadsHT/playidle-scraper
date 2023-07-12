import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from playidle.playIdle import PlayIdle

from pprint import pprint

import configparser

config = configparser.ConfigParser()
config.read("config.ini")

username = config.get("Creds", "username")
password = config.get("Creds", "password")

root_url = "https://www.playidle.com"
page_urls = {
    "login": f"{root_url}/login",
    "dashboard": f"{root_url}/dashboard",
    "bank": f"{root_url}/bank",
    "coinflip": f"{root_url}/coinflip",
}

element_ids = {
    "username": "username",
    "password": "password",
    "submit_button": "submit",
    "energy_element": "load_energy",
    "wallet_amount_element": "load_money",
    "deposit_button": "deposit",
    "deposit_input": "inputDeposit",
    "withdraw_button": "withdraw",
    "withdraw_input": "inputWithdrawal",
    "wager": "wager",
    "job_button": "jobButton",
}


# Configure the Selenium WebDriver to use Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(options=chrome_options)

driver.implicitly_wait(10)
driver.set_script_timeout(10)

pi = PlayIdle(driver, page_urls, element_ids)

# Logging in
if pi.login(username, password):
    print("Login successful")
else:
    print("Login failed")

pi.bank.deposit_money()

starting_wallet_amount = pi.player.get_wallet_amount()
print(f"Starting wallet amount: {starting_wallet_amount}")

starting_energy = pi.player.get_energy()
print(f"Starting player energy: {starting_energy}")

# Clicks on the job button until we run out of energy
player_energy = starting_energy
while player_energy % 100 != 0:
    player_energy = pi.player.get_energy()
    pi.job.click_job()
    time.sleep(0.5)


wallet_diff = pi.player.get_wallet_amount() - starting_wallet_amount
print(f"Gained: ${wallet_diff}")

energy_diff = starting_energy - player_energy
print(f"Energy lost: {energy_diff}")

pi.bank.deposit_money()

# Close the browser
driver.quit()
