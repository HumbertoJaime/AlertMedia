import pytest
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.home_page import HomePage


with open("config.json", "r") as config_file:
    config = json.load(config_file)

@pytest.fixture(scope="module")
def driver():
    service = Service(executable_path=config["driver_path"])
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver  
    driver.quit()

@pytest.fixture(scope="module")
def open_amazon(driver):
    # Carga la página de Amazon
    driver.get(config["base_url"])
    return HomePage(driver)  