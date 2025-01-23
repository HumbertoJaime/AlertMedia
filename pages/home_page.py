from selenium.webdriver.common.by import By
from pages.login_page import LoginPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
    
    def search_item(self, item):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox") 
        search_box.clear()
        search_box.send_keys(item)
        search_button = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_button.click()
    
    def go_to_login_page(self):
        login_button = self.driver.find_element(By.ID, "nav-link-accountList-nav-line-1")
        login_button.click()
        return LoginPage(self.driver)
    

